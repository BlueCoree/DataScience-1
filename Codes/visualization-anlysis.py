import pandas as pd
import plotly.express as px
import Ekstrak_Database

df = Ekstrak_Database.get_data()

if df is None or df.empty:
    print("Data tidak ditemukan. Periksa koneksi ke database.")
    exit()

selected_year_range = []
selected_genres = []

filtered_df = df.copy()

if filtered_df.empty:
    print("Data setelah filter kosong. Coba rentang tahun atau genre lain.")
else:
    print(f"Jumlah data setelah filter: {len(filtered_df)}")
    print(filtered_df.head())


  
total_revenue = filtered_df['revenue'].sum()
average_budget = filtered_df['budget'].mean()
most_popular_film = filtered_df.loc[filtered_df['revenue'].idxmax(), 'title']

print("\nStatistik Utama:")
print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Rata-rata Budget: ${average_budget:,.0f}")
print(f"Film Terpopuler: {most_popular_film}")

show_raw_data = True
if show_raw_data:
    print("\nData Mentah yang Difilter:")
    print(filtered_df)
