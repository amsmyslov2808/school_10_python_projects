CREATE TABLE plant_species
(
    id INTEGER PRIMARY KEY,
    species_name VARCHAR(100) NOT NULL,
    family_name VARCHAR(100) NOT NULL,
    climate VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL
);


CREATE TABLE plants
(
    id INTEGER PRIMARY KEY,
    plant_name VARCHAR(100) NOT NULL,
    planting_date DATE NOT NULL,
    height_cm NUMERIC(6, 2) NOT NULL,
    species_id INTEGER NOT NULL,

    FOREIGN KEY (species_id)
        REFERENCES plant_species(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);


INSERT INTO plant_species
    (id, species_name, family_name, climate, description)
VALUES
    (1, 'Роза', 'Розовые', 'Умеренный', 'Декоративное цветущее растение'),
    (2, 'Кактус', 'Кактусовые', 'Засушливый', 'Растение, способное запасать воду'),
    (3, 'Фикус', 'Тутовые', 'Тропический', 'Популярное комнатное растение'),
    (4, 'Орхидея', 'Орхидные', 'Тропический', 'Растение с яркими цветами'),
    (5, 'Лаванда', 'Яснотковые', 'Средиземноморский', 'Ароматное цветущее растение'),
    (6, 'Папоротник', 'Папоротниковые', 'Влажный', 'Тенелюбивое декоративное растение');


INSERT INTO plants
    (id, plant_name, planting_date, height_cm, species_id)
VALUES
    (1, 'Красная роза', '2025-04-15', 45.50, 1),
    (2, 'Белая роза', '2025-05-10', 38.00, 1),
    (3, 'Домашний кактус', '2024-08-20', 16.70, 2),
    (4, 'Фикус Бенджамина', '2023-03-12', 125.00, 3),
    (5, 'Белая орхидея', '2025-01-25', 42.30, 4),
    (6, 'Садовая лаванда', '2024-06-05', 55.00, 5),
    (7, 'Комнатный папоротник', '2025-02-17', 34.80, 6),
    (8, 'Розовая орхидея', '2024-11-08', 48.20, 4);