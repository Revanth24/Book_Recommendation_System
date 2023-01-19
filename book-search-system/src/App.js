import React, { Component } from "react";
import { Routes, Route } from "react-router-dom";
import Books from "./components/Books";
import BookDetails from "./components/BookDetails";

class App extends Component {
  render() {
    return (
      <Routes>
        <Route path="/" element={<Books />} />
        <Route path="/books/:id" element={<BookDetails />} />
      </Routes>
    );
  }
}

export default App;
