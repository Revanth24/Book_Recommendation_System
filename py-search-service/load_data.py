import pandas as pd
from convertors import clean
from convertors import helpfulness_converter, review_summary_converter, review_text_converter
from convertors import published_date_converter, book_title_converter, book_description_converter

PATH = 'archive'

class DataLoader:
    _books_df = None
    _ratings_df = None
    _pivot_table = None

    def load_dataset():
        use_cols_books = ['ID', 'Title', 'description', 'authors', 'publishedDate', 'categories',
                          'ratingsCount']

        use_cols_ratings = ['Id', 'ID', 'Price', 'User_id', 'review/helpfulness',
                            'review/score', 'review/time', 'review/summary', 'review/text']

        ratings = pd.read_csv(PATH + '/ratings.csv', usecols=use_cols_ratings,
                              converters={'review/helpfulness': helpfulness_converter,
                                          'review/summary': review_summary_converter,
                                          'review/text': review_text_converter})

        books = pd.read_csv(PATH + '/books.csv', usecols=use_cols_books,
                            converters={'publishedDate': published_date_converter,
                                        'Title': book_title_converter,
                                        'description': book_description_converter})

        DataLoader._books_df, DataLoader._ratings_df = clean(books, ratings)


if __name__ == '__main__':
    DataLoader.load_dataset()
    print(DataLoader._books_df.shape)
    print(DataLoader._ratings_df.shape)
    print(DataLoader._books_df.columns)
    print(DataLoader._ratings_df.columns)
