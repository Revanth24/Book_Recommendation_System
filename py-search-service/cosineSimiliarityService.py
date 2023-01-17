from convertors import book_title_converter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from load_data import DataLoader

NO_OF_RESULTS = 4

class _tfidfVec:
    _instance = None
    _vectorizer = None
    _term_frequencies = None

    def predict(self, search_title):
        query_vec = _tfidfVec._vectorizer.transform([book_title_converter(search_title)])
        similarity = cosine_similarity(query_vec, _tfidfVec._term_frequencies).flatten()
        indices = similarity.argsort()[::-1][:NO_OF_RESULTS]
        results = DataLoader._books_df.iloc[indices]['ID']
        return results.tolist()


def cosine_similiarity_service():
    if _tfidfVec._instance is None:
        _tfidfVec._instance = _tfidfVec()
        _tfidfVec._vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
        _tfidfVec._term_frequencies = _tfidfVec._vectorizer.fit_transform(DataLoader._books_df['Title'])

    return _tfidfVec._instance

