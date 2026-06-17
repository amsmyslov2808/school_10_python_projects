create table authors
(
    id     integer generated always as identity
        constraint authors_pkey
            primary key,
    fio    varchar(50) not null,
    rating real        not null,
    age    integer     not null
);

alter table authors
    owner to postgres;

INSERT INTO public.authors (fio, rating, age) VALUES ('Пушкин', 5, 34);
INSERT INTO public.authors (fio, rating, age) VALUES ('Достоевский', 4.9, 55);
INSERT INTO public.authors (fio, rating, age) VALUES ('Карамзин', 4.5, 40);

create table books
(
    id        integer generated always as identity
        constraint books_pkey
            primary key,
    title     varchar(50) not null,
    price     integer     not null,
    author_id integer     not null
        constraint fk_books_authors_author_id
            references authors
            on update restrict on delete restrict
);

alter table books
    owner to postgres;

INSERT INTO public.books (title, price, author_id) VALUES ('Руслан и людмила', 230, 1);
INSERT INTO public.books (title, price, author_id) VALUES ('Сборник стихов поэтов золотого века', 500, 1);
INSERT INTO public.books (title, price, author_id) VALUES ('Преступление и наказание', 1000, 2);

-- SELECT b.id, b.title, a.fio FROM books as b
-- JOIN authors as a
-- ON a.id = b.author_id

-- SELECT * FROM books as b
-- JOIN authors as a
-- ON a.id = b.author_id
-- -- WHERE b.price >700
-- WHERE a.age>40

-- SELECT * FROM books as b
-- RIGHT JOIN authors as a
-- ON a.id = b.author_id

-- SELECT * FROM authors as a
-- LEFT JOIN books as b
-- ON a.id = b.author_id


-- SELECT title, author_id FROM books WHERE author_id IN (SELECT id FROM authors WHERE rating>=4.5)

-- SELECT b.title, b.author_id FROM authors as a
-- JOIN books as b
-- ON a.id = b.author_id
-- WHERE a.rating>=4.5