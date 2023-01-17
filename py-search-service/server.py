from flask import Flask, jsonify, request
from cosineSimiliarityService import cosine_similiarity_service
from recommentByTitleService import by_title_recommender_service
from load_data import DataLoader

myapp = Flask(__name__)


@myapp.route("/predict", methods=["GET"])
def predict():
    params = request.args
    search_title = params.get("search_title", type=str)
    if search_title is None:
        return jsonify([])

    cs = cosine_similiarity_service()
    predictions = cs.predict(search_title)
    response = {"Predictions": predictions}
    return jsonify(response)


@myapp.route("/recommendByTitle", methods=["GET"])
def recommendByTitle():
    params = request.args
    index = params.get("id", type=int)
    if index is None:
        return jsonify([])

    btr = by_title_recommender_service()
    predictions = btr.predict(index)
    int_ids = [int(x) for x in predictions]
    response = {"Predictions": int_ids}
    return jsonify(response)


if __name__ == "__main__":
    DataLoader.load_dataset()
    myapp.run(host="0.0.0.0", port=8083,debug=False)
