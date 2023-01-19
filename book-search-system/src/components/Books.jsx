import React, { Component } from "react";
import Book from "./Book";
import SearchIcon from "../search.svg";
import { Link } from "react-router-dom";
import { Container } from "react-bootstrap";

class Books extends Component {
  state = {
    loading: true,
    books: [],
    search_term: "",
  };

  async componentDidMount() {
    this.searchBooks("");
  }

  searchBooks = async (search_query) => {
    const url = "http://127.0.0.1:8082/search?q=" + search_query;
    const response = await fetch(url);
    const data = await response.json();
    this.setState({ books: data, loading: false });
    console.log(data);
  };

  render() {
    return (
      <Container>
        <div className="app">
          <h1>Boogle</h1>
          <div className="search">
            <input
              placeholder="Search for books"
              value={this.state.search_term}
              onChange={(e) => this.setState({ search_term: e.target.value })}
            ></input>
            <img
              src={SearchIcon}
              onClick={() => this.searchBooks(this.state.search_term)}
            ></img>
          </div>

          <div className="container">
            {this.state.loading ? (
              <h1>Loading</h1>
            ) : (
              this.state.books.map((book) => (
                <Link key={book.id} to={"/books/" + book.id}>
                  <Book book={book}></Book>
                </Link>
              ))
            )}
          </div>
        </div>
      </Container>
    );
  }
}

export default Books;
