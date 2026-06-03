-- Table: public.cars

-- DROP TABLE IF EXISTS public.cars;

CREATE TABLE IF NOT EXISTS public.cars
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    brand character varying(50) COLLATE pg_catalog."default" NOT NULL,
    model character varying(50) COLLATE pg_catalog."default" NOT NULL,
    price integer NOT NULL,
    release_year integer NOT NULL,
    engine_size real NOT NULL,
    CONSTRAINT cars_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cars
    OWNER to postgres;



------

INSERT INTO cars (brand, model, price, release_year, engine_size)
VALUES 
('Mercedes-Banz', 'GLE Купе', 3500000, 2019, 2.4),
('BMW', 'M3', 2400000, 2014, 1.5),
('FORD', 'Focus', 1300000, 2011, 1.3)

SELECT * FROM cars

UPDATE cars SET price=2000000 WHERE id=3

DELETE FROM cars WHERE id=1