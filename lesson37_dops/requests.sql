-- SELECT * FROM studios

-- SELECT * FROM users WHERE age>15

-- SELECT * FROM movies ORDER BY price DESC LIMIT 3

-- SELECT * FROM movies ORDER BY release_year DESC LIMIT 1

-- SELECT * FROM movies WHERE title LIKE '%баг%'

-- SELECT * FROM users WHERE age BETWEEN 15 and 16

-- SELECT * FROM user_movies WHERE watched_at BETWEEN '2026-04-01' and '2026-05-31'

-- SELECT * FROM users WHERE city IN ('Брянск','Москва','Курск')

-- SELECT DISTINCT(city) FROM users

-- SELECT COUNT(DISTINCT(city)) FROM users

-- SELECT COUNT(DISTINCT(city)) as unique_city_count FROM users

-- SELECT COUNT(DISTINCT(city)) as "unique city count" FROM users

-- INSERT INTO studios (name, country, rating) VALUES ('XXX', 'YYY', 5.0)

-- UPDATE users SET balance = balance + 300 WHERE nickname = 'kirill_stream'

-- SELECT * FROM users WHERE nickname = 'kirill_stream'

-- SELECT m.*, s.name FROM movies as m
-- JOIN studios as s
-- ON m.studio_id = s.id

-- SELECT m.*,s.name FROM movies as m
-- JOIN studios as s
-- ON m.studio_id = s.id
-- WHERE m.id IN (SELECT movie_id FROM user_movies WHERE user_id = (SELECT id FROM users WHERE nickname='sveta_cinema'))

-- SELECT * FROM users WHERE id IN
-- (SELECT DISTINCT(u.id) FROM user_movies as um
-- JOIN users as u
-- ON um.user_id = u.id
-- JOIN movies as m
-- ON um.movie_id = m.id
-- WHERE m.price>300)

-- SELECT * FROM users WHERE id IN (SELECT user_id FROM user_movies WHERE movie_id IN (SELECT id FROM movies WHERE price > 300))





