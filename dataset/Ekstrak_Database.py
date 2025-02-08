import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql


def create_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='bluecore',
            database='dummyproject_1'
        )
        print("Koneksi ke MySql berhasil!")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error: '{e}")
        return None

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query berhasil dieksekusi!")
    except pymysql.MySQLError as e:
        print(f"Error: '{e}")
    finally:
        cursor.close()

def read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()

def get_data():
    conn = create_connection()
    if conn:
        query = """
            SELECT 
                b.box_office_id, 
                b.movie_id, 
                b.country, 
                b.revenue AS total_revenue, 
                m.release_year, 
                m.genre,
                m.budget,
                m.title 
            FROM 
                box_office AS b 
            JOIN 
                movies AS m 
            ON 
                b.movie_id = m.movie_id;
            """
        result = read_query(conn, query)
        conn.close()
    if result:
        df = pd.DataFrame(result, columns=['box_office_id', 'movie_id', 'country', 'total_revenue', 'release_year', 'genre', 'budget', 'title'])
        df['total_revenue'] = df['total_revenue'].astype(float)
        df.rename(columns={'total_revenue': 'revenue'}, inplace=True)
        return df
    else:
        print("Tidak ada data yang diambil!")
        return None

df = get_data()
df_limited = df.nlargest(15, 'revenue')

if df is not None:
    plt.figure(figsize=(16, 8))
    sns.barplot(x='title', y='revenue', data=df_limited)
    plt.title('Revenue per Film 3D')
    plt.xticks(rotation=10, ha='right')
    plt.show()

else:
    print("Error")


print("Data awal (5 baris teratas):")
print(df.head())
print("\nStatistik Data:")
print(df.describe(include='all'))
print("\nNilai unik dalam kolom 'genre':", df['genre'].unique())



