-- INSERT INTO workers (fio, profession, experience,rating,salary)
-- VALUES 
-- ('Иванов Алексей Игоревич', 'Программист', 5, 4.8, 180000),
-- ('Petрова Мария Сергеевна', 'Маркетолог', 2, 4.2, 90000),
-- ('Сидоров Дмитрий Николаевич', 'Аналитик данных', 7, 4.9, 220000),
-- ('Кузнецова Анна Владимировна', 'Дизайнер', 3, 4.5, 110000),
-- ('Смирнов Игорь Олегович', 'Тестировщик', 1, 4.0, 75000)

-- SELECT * FROM workers

-- SELECT profession, salary FROM workers

-- SELECT * FROM workers WHERE salary>=100000 AND rating>=4.5

-- SELECT * FROM workers WHERE salary>=100000 OR experience<3

-- SELECT * FROM workers ORDER BY salary DESC

-- SELECT * FROM workers
-- ORDER BY id
-- LIMIT 3
-- OFFSET 2

-- SELECT * FROM workers WHERE id=3

-- SELECT COUNT(id) FROM workers

-- SELECT COUNT(id) AS count_richest_workers FROM workers WHERE salary>=100000

-- SELECT SUM(salary) FROM workers WHERE experience>=5

-- SELECT AVG(experience) FROM workers

-- SELECT MAX(salary) FROM workers

-- SELECT NOW()

-- SELECT ROUND(AVG(experience), 1) FROM workers

-- SELECT * FROM workers WHERE salary = (SELECT MAX(salary) FROM workers)


SELECT * FROM workers