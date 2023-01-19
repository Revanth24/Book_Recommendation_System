import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "../css/bookdetails.css";

export default function BookInfoCard(props) {
  const { id } = useParams();
  const book = props.book;

  return book ? (
    <>
      <div className="card-wrapper">
        <div className="card">
          <div className="book-img">
            {book.imgURL === "" ? (
              <>
                <p>No img</p>
              </>
            ) : (
              <>
                <img src={book.imgURL}></img>
              </>
            )}
          </div>
          <div className="book-detail">
            <div className="book-title">
              <h2>{book.title}</h2>
            </div>
            <div className="book-authors">
              <p>{book.authors}</p>
            </div>
            <div className="book-categories">
              <span>{book.categories}</span>
            </div>
            <div className="book-description">
              <h2>About this book</h2>
              <p>{book.description}</p>
            </div>
          </div>
        </div>
      </div>
    </>
  ) : (
    <h1>{id}</h1>
  );
}
