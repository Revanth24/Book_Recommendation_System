create table books (
id int primary key ,
title text,
total_review_count text,
description text,
authors text,
image text,
preview_link text,
publisher text,
published_date text,
info_link text,
categories text,
ratingcount text);

COPY books(id, title, total_review_count, description, authors, image, preview_link, publisher, published_date, info_link, categories, ratingcount) FROM '/archive/books.csv' DELIMITER ',' CSV HEADER;
