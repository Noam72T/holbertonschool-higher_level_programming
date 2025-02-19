from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

# Main Route
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

# Route of the user data (List of users)
@app.route('/data')
def data():
    return jsonify(list(users))


# Route of the status
@app.route("/status", methods=['GET'])
def status():
    return "OK"

# Route of the user data (Single user)
@app.route('/users/<username>')
def username(username):
    if username is None:
        return jsonify({'error': 'Username is required'}), 400
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

# Route to add a new user


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if data is None or data.get('username') is None:
        return jsonify({'error': 'Username is required'}), 400
    user = {
        'username': data.get('username'),
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[user.get('username')] = user
    return jsonify({'message': 'User added', 'user': user}), 201

if __name__ == "__main__":
    app.run(debug=True)
