# app.py
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuring server-side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)  # Enable CORS for all routes

# Sample in-memory data store
data_store = {
    'users': [],
    'messages': []
}

# ---------------------- BASIC RESTFUL APIs ----------------------

# GET - Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data_store['users'])

# POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    data_store['users'].append(data)
    return jsonify({'message': 'User added', 'user': data}), 201

# PUT - Update a user by index
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id < len(data_store['users']):
        data_store['users'][user_id] = data
        return jsonify({'message': 'User updated', 'user': data})
    return jsonify({'error': 'User not found'}), 404

# DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id < len(data_store['users']):
        removed = data_store['users'].pop(user_id)
        return jsonify({'message': 'User removed', 'user': removed})
    return jsonify({'error': 'User not found'}), 404

# ---------------------- SESSION HANDLING ----------------------

# Login (set session)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    session['user'] = username
    return jsonify({'message': f'Logged in as {username}'})

# Check session (get current user)
@app.route('/session', methods=['GET'])
def get_session():
    if 'user' in session:
        return jsonify({'logged_in': True, 'user': session['user']})
    return jsonify({'logged_in': False})

# Logout (clear session)
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'})

# ---------------------- MESSAGE POSTING EXAMPLE ----------------------

# POST a message
@app.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    data_store['messages'].append(data)
    return jsonify({'message': 'Message added', 'data': data})

# GET all messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(data_store['messages'])

# ---------------------- MAIN ----------------------

if __name__ == '__main__':
    app.run(debug=True)
