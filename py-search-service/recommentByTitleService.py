from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from load_data import DataLoader

POPULARITY_THRESHOLD = 2000
KNN_MODEL_METRIC = 'cosine'
KNN_MODEL_ALGORITHM = 'auto'
KNN_MODEL_NNEIGHBOURS = 6
PREDICT_NNEIGHBOURS = 9


class ByTitleRecommenderService:
    _instance = None
    _model = None
    _pivot_table = None

    def _create_sparse_pivot():
        ByTitleRecommenderService._pivot_table = DataLoader._ratings_df.pivot_table(columns='User_id', index='ID',
                                                                                  values="review/score")
        ByTitleRecommenderService._pivot_table.fillna(0, inplace=True)
        return csr_matrix(ByTitleRecommenderService._pivot_table.values)

    def get_trained_knn():
        sparse_mat = ByTitleRecommenderService._create_sparse_pivot()
        model = NearestNeighbors(metric=KNN_MODEL_METRIC, algorithm=KNN_MODEL_ALGORITHM,
                                 n_neighbors=KNN_MODEL_NNEIGHBOURS)
        model.fit(sparse_mat)
        return model

    def predict(self, index):
        print('value received {0}'.format(index))
        print('pivot length: {0}'.format(len(ByTitleRecommenderService._pivot_table)))
        if 0 > index or index >= len(ByTitleRecommenderService._pivot_table):
            return []

        distances, indices = ByTitleRecommenderService._model.kneighbors(
            ByTitleRecommenderService._pivot_table.iloc[index, :].values.reshape(1, -1),
            n_neighbors=PREDICT_NNEIGHBOURS + 1)

        books_title = DataLoader._books_df['ID']
        indices = indices.squeeze()

        results = list(map(lambda x: books_title[x], indices))
        results.remove(index)
        return results


def by_title_recommender_service():
    if ByTitleRecommenderService._instance is None:
        ByTitleRecommenderService._instance = ByTitleRecommenderService()
        ByTitleRecommenderService._model = ByTitleRecommenderService.get_trained_knn()
    return ByTitleRecommenderService._instance
