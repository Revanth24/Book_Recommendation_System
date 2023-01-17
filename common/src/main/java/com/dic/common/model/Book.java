package com.dic.common.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "books")
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;

    private String title;

    private String description;

    private String authors;

    @Column(name = "image")
    private String imgURL;

    @Column(name = "preview_link")
    private String previewLink;

    private String publisher;

    private String published_date;
    @Column(name = "info_link")
    private String info_date;

    private String categories;

    @Column(name = "ratingcount")
    private String ratingsCount;

    public Book() {

    }

    public Book(int id, String title, String description, String authors, String imgURL,
                String previewLink, String publisher, String categories, String ratingsCount) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.authors = authors;
        this.imgURL = imgURL;
        this.previewLink = previewLink;
        this.publisher = publisher;
        this.categories = categories;
        this.ratingsCount = ratingsCount;
    }
}
