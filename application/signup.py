from application.models import User
from flask import jsonify

def signup_user(request):
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required'}), 400
    
    if User.find_by_username(username):
        return jsonify({'error': 'Username already exists'}), 400
    
    new_user = User(username, email, password)
    new_user.save()
    
    return jsonify({'message': 'User created successfully'}), 201