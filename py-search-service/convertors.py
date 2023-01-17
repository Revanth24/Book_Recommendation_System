import string

import nltk
import pandas as pd
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Reference: https://www.analyticsvidhya.com/blog/2020/04/beginners-guide-exploratory-data-analysis-text-data/

contractions_dict = {"ain't": "are not", "'s": " is", "aren't": "are not",
                     "can't": "cannot", "can't've": "cannot have",
                     "'cause": "because", "could've": "could have", "couldn't": "could not",
                     "couldn't've": "could not have", "didn't": "did not", "doesn't": "does not",
                     "don't": "do not", "hadn't": "had not", "hadn't've": "had not have",
                     "hasn't": "has not", "haven't": "have not", "he'd": "he would",
                     "he'd've": "he would have", "he'll": "he will", "he'll've": "he will have",
                     "how'd": "how did", "how'd'y": "how do you", "how'll": "how will",
                     "I'd": "I would", "I'd've": "I would have", "I'll": "I will",
                     "I'll've": "I will have", "I'm": "I am", "I've": "I have", "isn't": "is not",
                     "it'd": "it would", "it'd've": "it would have", "it'll": "it will",
                     "it'll've": "it will have", "let's": "let us", "ma'am": "madam",
                     "mayn't": "may not", "might've": "might have", "mightn't": "might not",
                     "mightn't've": "might not have", "must've": "must have", "mustn't": "must not",
                     "mustn't've": "must not have", "needn't": "need not",
                     "needn't've": "need not have", "o'clock": "of the clock", "oughtn't": "ought not",
                     "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not",
                     "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have",
                     "she'll": "she will", "she'll've": "she will have", "should've": "should have",
                     "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have",
                     "that'd": "that would", "that'd've": "that would have", "there'd": "there would",
                     "there'd've": "there would have", "they'd": "they would",
                     "they'd've": "they would have", "they'll": "they will",
                     "they'll've": "they will have", "they're": "they are", "they've": "they have",
                     "to've": "to have", "wasn't": "was not", "we'd": "we would",
                     "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have",
                     "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will",
                     "what'll've": "what will have", "what're": "what are", "what've": "what have",
                     "when've": "when have", "where'd": "where did", "where've": "where have",
                     "who'll": "who will", "who'll've": "who will have", "who've": "who have",
                     "why've": "why have", "will've": "will have", "won't": "will not",
                     "won't've": "will not have", "would've": "would have", "wouldn't": "would not",
                     "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would",
                     "y'all'd've": "you all would have", "y'all're": "you all are",
                     "y'all've": "you all have", "you'd": "you would", "you'd've": "you would have",
                     "you'll": "you will", "you'll've": "you will have", "you're": "you are",
                     "you've": "you have"}


def helpfulness_converter(value):
    if '/' not in value:
        print('Not a valid value', value)
        return 0

    dividend, divisor = value.split('/')
    if dividend == '0' and divisor == '0':
        return 0

    if divisor == '0':
        print('Divide by zero!!', value)
        return 0

    if int(dividend) > int(divisor):
        return 0;

    return int(dividend) / int(divisor)


def stop_words_removal(value):
    words = []
    for word in value.split():
        if word not in stop_words:
            words.append(word)

    return " ".join(words)


def remove_punctuation(value):
    return value.translate(str.maketrans('', '', string.punctuation))


def convert_to_lowercase(value):
    return value.lower()


def remove_whitespace(value):
    return value.strip()


def fix_contractions(value):
    words = []
    for word in value.split():
        words.append(contractions_dict.get(word, word))

    return " ".join(words)


def normal_text_cleanup(value):
    value = fix_contractions(value)
    value = remove_punctuation(value)
    value = convert_to_lowercase(value)
    value = remove_whitespace(value)
    return value


def review_summary_converter(value):
    value = normal_text_cleanup(value)
    return stop_words_removal(value)


def review_text_converter(value):
    value = normal_text_cleanup(value)
    return stop_words_removal(value)


def review_book_title_converter(value):
    value = normal_text_cleanup(value)
    return value


def book_title_converter(value):
    return normal_text_cleanup(value)


def book_description_converter(value):
    value = normal_text_cleanup(value)
    return stop_words_removal(value)


def published_date_converter(x):
    x = str(x)[:10]
    if x.lower() == 'nan':
        return 'nan'
    date = x.split('-')
    if len(date[0]) < 4 or any(not c.isalnum() for c in date[0][:4]):
        return 'nan'
    year, month, day = date[0][:4], "01", "01"
    if len(date) > 1:
        month = date[1][:2]
    if len(date) > 2:
        day = date[2][:2]
    df = pd.DataFrame({'year': [int(year)],
                       'month': [int(month)],
                       'day': [int(day)]})
    return pd.to_datetime(df, errors='coerce')


def clean(books, ratings):
    ratings.dropna(axis=0, how='any', subset=['review/summary', 'review/text'], inplace=True)
    #books.dropna(axis=0, how='any', subset=['publishedDate'], inplace=True)
    books.fillna(value={'description': '', 'authors': '', 'ratingsCount': 0, 'categories': '[\'Misc\']', 'Price': 0, 'publishedDate':''}, inplace=True)
    temp = pd.DataFrame(books[['ID', 'categories']]).set_index('ID')
    all_ratings_categories = ratings.join(temp, on=['ID'], how='left', lsuffix='_avg', rsuffix='_ratings')
    #all_ratings_categories['review/time'] = pd.to_datetime(all_ratings_categories['review/time'], unit='s').dt.date

    return books, all_ratings_categories