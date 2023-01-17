package com.dic.bookservice.controller;

import com.dic.bookservice.service.BooksService;
import com.dic.common.model.Book;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.util.*;

@RestController
public class BookController {

    @Autowired
    BooksService booksService;

    @GetMapping("/")
    public String hello() {
        return "hello";
    }

    @GetMapping("/books/{id}")
    public Book getBook(@PathVariable int id) {

        Book book = booksService.getBookById(id);

        if (book == null)
            throw new ResponseStatusException(HttpStatus.NOT_FOUND);

        return book;
    }

    @PostMapping("/books")
    public Collection<Book> getBook(@RequestBody String ids) {

        StringBuilder str = new StringBuilder(ids);
        str.deleteCharAt(ids.length() - 1);
        str.deleteCharAt(0);

        String[] idsArr = str.toString().split(",");

        List<Integer> bookIds = new LinkedList();
        for (String id: idsArr) {
            bookIds.add(Integer.parseInt(id));
        }
        System.out.println(bookIds);
        List<Book> books = booksService.getBooks(bookIds);
        return booksService.sortBooks(bookIds, books);
    }
}
