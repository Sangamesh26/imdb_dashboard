from flask import jsonify
from pymongo import MongoClient
import json

DEFAULT_LIMIT = 20
DEFAULT_OFFSET = 1

client = MongoClient('mongodb://localhost:27017/')
db = client['imdb']

def get_movie_list(request):
    limit = int(request.args.get("limit",DEFAULT_LIMIT))
    offset = int(request.args.get("offset",DEFAULT_OFFSET))
    
    movies = db.uploads.find().skip((offset - 1) * limit).limit(limit)
    movie_list = [movie['data'] for movie in movies]
    
    json_data = jsonify(movie_list)

    return json_data
    