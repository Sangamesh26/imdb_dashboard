from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['imdb']

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # We can hash the password and store, for now, I am just having password and the hash for it
    def save(self):
        db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password': self.password
        })

    @staticmethod
    def find_by_username(username):
        user_data = db.users.find_one({'username': username})
        return User(user_data['username'], user_data['email'], user_data['password']) if user_data else None

    def check_password(self, password):
        if self.password == password:
            return True
        return False
