fig1 = px.scatter(
    filtered_df,
    x="budget",
    y="revenue",
    size="revenue",
    color="genre",
    hover_name="title",
    log_x=True,
    log_y=True,
    title="Budget vs Revenue Film 3D"
)
fig1.write_html("budget_vs_revenue.html")
print("Plot 'Budget vs Revenue' disimpan sebagai 'budget_vs_revenue.html'")

fig2 = px.bar(
    filtered_df,
    x="release_year",
    y="revenue",
    color="genre",
    hover_name="title",
    title="Tren Pendapatan Film 3D dari Tahun ke Tahun"
)
fig2.write_html("trend_revenue.html")
print("Plot 'Tren Pendapatan Tahun ke Tahun' disimpan sebagai 'trend_revenue.html'")

country_mapping = {
    "USA": "USA",
    "China": "CHN",
    "Indonesia": "IDN",
    "Malaysia": "MYS",
    "Hong Kong": "HKG",
    "Singapore": "SGP"
}

fig3 = px.choropleth(
    filtered_df,
    locations="country",
    color="revenue",
    hover_name="country",
    projection="natural earth",
    title="Distribusi Penonton Film 3D Global"
)

filtered_df['country'] = filtered_df['country'].replace(country_mapping)
fig3.write_html("viewer_distribution.html")
print("Plot 'Distribusi Penonton Global' disimpan sebagai 'viewer_distribution.html'") #for this code, I'm still confused why the result only shows USA, but none the rest. I've already tried many ways but still can't figure it out :(
