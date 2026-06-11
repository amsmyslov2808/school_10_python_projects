-- Table: public.students

-- DROP TABLE IF EXISTS public.students;

CREATE TABLE IF NOT EXISTS public.students
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    age integer NOT NULL,
    group_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    average_score real NOT NULL,
    CONSTRAINT students_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.students
    OWNER to postgres;

-- SELECT * FROM public.students WHERE group_name = 'Python-1'

-- SELECT group_name, round(avg(average_score)::numeric,2) as round_score FROM students 
-- GROUP BY group_name
-- HAVING avg(average_score) > 4.5

-- SELECT group_name, round(avg(average_score)::numeric,2) as round_score
-- FROM students
-- WHERE average_score>=4
-- GROUP BY group_name

-- SELECT COUNT(DISTINCT(group_name)) FROM students 

-- SELECT * FROM students WHERE average_score = (SELECT min(average_score) FROM students)
