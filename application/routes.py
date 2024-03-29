from application import app
from application.login import login_user
from application.signup import signup_user
from application.upload_csv import upload_movies_csv
from application.upload_status import upload_status
from application.movie_list import get_movie_list
from flask import jsonify,request

@app.route("/", methods=['GET'])
def index():
    return jsonify({"message":"Welcome to IMDB"})

# Good to have the health check
@app.route("/health", methods=['GET'])
def health_check():
    return jsonify({"message":"All Good!"})

# Route for user signup
@app.route("/signup", methods=['POST'])
def sign_up_user():
    return signup_user(request)

# Route for user login
@app.route("/login", methods=['POST'])
def log_in_user():
    return login_user(request)

# Route to upload the csv
@app.route("/upload_csv", methods=['POST'])
def upload_csv():
    return upload_movies_csv(request)

@app.route("/fetch_csv_status/<task_id>", methods=['GET'])
def get_upload_csv_status(task_id):
    return upload_status(task_id)

@app.route("/get_content", methods=['GET'])
def get_imdb_content():
    return get_movie_list(request)
