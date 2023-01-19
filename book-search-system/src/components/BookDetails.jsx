import { useEffect, useState, useCallback } from "react";
import { useParams } from "react-router-dom";
import "../css/bookdetails.css";
import BookInfoCard from "./BookInfoCard";
import BookSuggestion from "./BookSuggestion";
import React from "react";

export default function BookDetails() {
  const { id } = useParams();
  const [suggestedBooks, setSuggestedBooks] = useState([]);
  const [bookInfo, setBookInfo] = useState();

  useEffect(() => {
    const recommendUrl = "http://127.0.0.1:8082/recommend?id=" + id;
    const bookInfoUrl = "http://127.0.0.1:8081/books/" + id;

    Promise.all([fetch(recommendUrl), fetch(bookInfoUrl)])
      .then(function (responses) {
        return Promise.all(
          responses.map(function (response) {
            return response.json();
          })
        );
      })
      .then(function (data) {
        setSuggestedBooks(data[0]);
        setBookInfo(data[1]);
      })
      .catch(function (error) {
        console.log(error);
      });
  }, []);

  const fetchRequest = async (id) => {
    const recommendUrl = "http://127.0.0.1:8082/recommend?id=" + id;
    const bookInfoUrl = "http://127.0.0.1:8081/books/" + id;
    Promise.all([fetch(recommendUrl), fetch(bookInfoUrl)])
      .then(function (responses) {
        return Promise.all(
          responses.map(function (response) {
            return response.json();
          })
        );
      })
      .then(function (data) {
        setSuggestedBooks(data[0]);
        setBookInfo(data[1]);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const handleSuggestionClick = (id) => {
    fetchRequest(id);
    window.scrollTo(0, 0);
  };

  return (
    <>
      <BookInfoCard book={bookInfo} />
      <BookSuggestion onClick={handleSuggestionClick} books={suggestedBooks} />
    </>
  );
}
