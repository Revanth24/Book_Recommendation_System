package com.dic.searchservice.controller;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class BookSearchController {

   @GetMapping("/search")
    public String getBooks(@RequestParam(required = false, name = "q") String searchQuery) {

        if (searchQuery.equals("")) {
            return "[]";
        }

        String pySearchURL = "http://py-search-service:8083/predict?search_title=" + searchQuery;
        String bookSearchURL = "http://book-service:8081/books";

        // Ask for book ids that match the title from py search service
        ResponseEntity<String> responseEntity = new RestTemplate().getForEntity(pySearchURL, String.class);
        String response = responseEntity.getBody();
        System.out.println(response);

        try {
            JSONObject jsonObject = new JSONObject(response);
            JSONArray jsonBooksArray = jsonObject.getJSONArray("Predictions");

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<String> entity = new HttpEntity<>(jsonBooksArray.toString(), headers);
            response = new RestTemplate().postForObject(bookSearchURL, entity, String.class);
        }catch (JSONException err){
           System.out.println(err);
        }

        return response;
   }

    @GetMapping("/recommend")
    public String getRecommendedBooks(@RequestParam(required = false, name = "id") String id) {

        System.out.println(id);

        String pySearchURL = "http://py-search-service:8083/recommendByTitle?id=" + id;
        String bookSearchURL = "http://book-service:8081/books";

        // Ask for book ids that match the title from py search service
        ResponseEntity<String> responseEntity = new RestTemplate().getForEntity(pySearchURL, String.class);
        String response = responseEntity.getBody();
        System.out.println(response);

        try {
            JSONObject jsonObject = new JSONObject(response);
            JSONArray jsonBooksArray = jsonObject.getJSONArray("Predictions");

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<String> entity = new HttpEntity<>(jsonBooksArray.toString(), headers);
            System.out.println(jsonBooksArray.toString());
            response = new RestTemplate().postForObject(bookSearchURL, entity, String.class);
            System.out.println(response);

        }catch (JSONException err){
            System.out.println(err);
        }

        return response;
   }

}
