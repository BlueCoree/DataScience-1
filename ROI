SELECT title, release_year,
	FORMAT(budget, 0) AS formatted_budget,
	FORMAT(SUM(revenue), 0) AS total_revenue,
    FORMAT((SUM(revenue) - budget) / budget * 100, 0) as ROI
FROM movies
JOIN box_office ON box_office.movie_id = movies.movie_id
GROUP BY movies.movie_id, title
ORDER BY (SUM(revenue) - budget) / budget * 100 DESC;
