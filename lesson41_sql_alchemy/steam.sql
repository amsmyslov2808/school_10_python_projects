-- Чтобы можно было запускать скрипт повторно
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_roles;

-- Таблица ролей пользователей
CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(500) NOT NULL
);

-- Таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    steam_level INTEGER NOT NULL,
    hours_played INTEGER NOT NULL,
    last_online TIMESTAMP NOT NULL,
    is_online BOOLEAN DEFAULT FALSE,

    role_id INTEGER NOT NULL,

    CONSTRAINT fk_user_role
        FOREIGN KEY (role_id)
        REFERENCES user_roles(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

INSERT INTO user_roles (role_name, description)
VALUES
('Новичок', 'Пользователь недавно зарегистрировался и почти не играет'),
('Игрок', 'Обычный активный пользователь Steam'),
('Коллекционер', 'Покупает много игр и собирает достижения'),
('Модератор', 'Следит за порядком в сообществе'),
('Администратор', 'Имеет расширенные права управления');

INSERT INTO users 
(nickname, email, steam_level, hours_played, last_online, is_online, role_id)
VALUES
('CyberWolf', 'cyberwolf@mail.com', 12, 340, '2026-06-24 18:30:00', TRUE, 2),
('DarkPixel', 'darkpixel@mail.com', 5, 75, '2026-06-23 21:15:00', FALSE, 1),
('GameHunter', 'gamehunter@mail.com', 48, 2300, '2026-06-24 16:10:00', TRUE, 3),
('SteamLord', 'steamlord@mail.com', 80, 5200, '2026-06-22 12:00:00', FALSE, 3),
('ModAlex', 'modalex@mail.com', 35, 1500, '2026-06-24 17:45:00', TRUE, 4),
('AdminMax', 'adminmax@mail.com', 100, 8000, '2026-06-24 19:00:00', TRUE, 5),
('NoobPlayer', 'noobplayer@mail.com', 1, 3, '2026-06-20 10:30:00', FALSE, 1),
('OldGamer', 'oldgamer@mail.com', 25, 980, '2026-06-21 14:20:00', FALSE, 2);