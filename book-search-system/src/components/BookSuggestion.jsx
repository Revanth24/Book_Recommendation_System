import React from "react";
import Book from "./Book";
import { Link } from "react-router-dom";
import { Container } from "react-bootstrap";
import { useParams } from "react-router-dom";

export default function BookSuggestion(props) {
  const { id } = useParams();
  const books = props.books;

  return (
    <Container>
      <div className="suggestion">
        <div className="sugg-title">
          <h2>People also read</h2>
        </div>
        <div className="container">
          {books.map((book) => (
            <Link key={book.id} to={"/books/" + book.id}>
              <Book onClick={props.onClick} book={book}></Book>
            </Link>
          ))}
        </div>
      </div>
    </Container>
  );
}
