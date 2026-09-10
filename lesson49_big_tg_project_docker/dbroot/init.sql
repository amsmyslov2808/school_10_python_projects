-- Таблица создаётся автоматически при первой инициализации контейнера PostgreSQL.
CREATE TABLE IF NOT EXISTS visited_cities
(
    -- Уникальный идентификатор записи генерируется базой данных.
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    tg_user_id bigint NOT NULL,
    name character varying(50) NOT NULL,
    arrival_date date NOT NULL,
    note character varying(1000) NOT NULL,
    CONSTRAINT visited_cities_pkey PRIMARY KEY (id)
)
