DROP TABLE IF EXISTS videos;
DROP TABLE IF EXISTS channels;

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    channel_name VARCHAR(100) NOT NULL,
    subscribers_count INTEGER NOT NULL,
    monthly_views INTEGER NOT NULL
);

CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    video_title VARCHAR(150) NOT NULL,
    duration_seconds INTEGER NOT NULL,
    views_count INTEGER NOT NULL,
    likes_count INTEGER NOT NULL,
    dislikes_count INTEGER NOT NULL,
    channel_id INTEGER NOT NULL,

    CONSTRAINT fk_videos_channels
        FOREIGN KEY (channel_id)
        REFERENCES channels(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

INSERT INTO channels 
(channel_name, subscribers_count, monthly_views)
VALUES
('Кодим Просто', 125000, 850000),
('Игровой Архив', 98000, 620000),
('Наука Каждый День', 210000, 1400000),
('Кулинарный Уголок', 76000, 430000),
('Истории Города', 54000, 310000),
('ТехноОбзор', 340000, 2200000),
('Музыка Без Границ', 180000, 970000),
('Путешествия Онлайн', 145000, 790000),
('Фитнес Дома', 67000, 380000),
('Школа Python', 112000, 690000);

INSERT INTO videos
(video_title, duration_seconds, views_count, likes_count, dislikes_count, channel_id)
VALUES
('Как написать первую программу на Python', 720, 85000, 5400, 120, 1),
('История старых компьютерных игр', 960, 67000, 4200, 95, 2),
('Почему светит Солнце', 840, 120000, 9100, 210, 3),
('Готовим пасту за 15 минут', 600, 45000, 2800, 60, 4),
('Заброшенные здания нашего города', 1100, 39000, 3100, 140, 5),
('Обзор нового смартфона', 780, 210000, 15400, 430, 6),
('Лучшие песни для учебы', 3600, 99000, 7300, 180, 7),
('Путешествие по Карелии', 1500, 76000, 6100, 130, 8),
('Тренировка на всё тело дома', 900, 52000, 3900, 85, 9),
('Что такое базы данных простыми словами', 1020, 88000, 6900, 110, 10);