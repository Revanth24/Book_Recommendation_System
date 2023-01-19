import React, { Component } from "react";

class Book extends Component {
  render() {
    return (
      <div
        onClick={() => this.props.onClick(this.props.book.id)}
        className="movie"
      >
        <div>
          <p>{this.props.book.authors}</p>
        </div>

        <div>
          {this.props.book.imgURL === "" || this.props.book.imgURL === null ? (
            <>
              <></>
              <img
                src={"https://via.placeholder.com/400"}
                alt={this.props.book.title}
              ></img>
            </>
          ) : (
            <>
              <img
                src={this.props.book.imgURL}
                alt={this.props.book.title}
              ></img>
            </>
          )}
        </div>
        <div>
          <span>{this.props.book.categories}</span>
          <h3>{this.props.book.title}</h3>
        </div>
      </div>
    );
  }
}

export default Book;
