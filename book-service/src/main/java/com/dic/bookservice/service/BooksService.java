package com.dic.bookservice.service;

import com.dic.bookservice.repository.BooksRepository;
import com.dic.common.model.Book;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class BooksService {

    @Autowired
    BooksRepository booksRepository;

    public Book getBookById(Integer id) {
        Optional<Book> byId = booksRepository.findById(id);
        return byId.get();
    }

    public List<Book> getBooks(List<Integer> ids) {
        return booksRepository.findAllById(ids);
    }

    public List<Book> sortBooks(List<Integer> ids, List<Book> books) {

        Map<Integer, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < ids.size(); i++) {
            indexMap.put(ids.get(i), i);
        }

        Collections.sort(books, new Comparator<Book>() {
            @Override
            public int compare(Book o1, Book o2) {
                return indexMap.get(o1.getId()) - indexMap.get(o2.getId());
            }
        });
        return books;
    }
}
