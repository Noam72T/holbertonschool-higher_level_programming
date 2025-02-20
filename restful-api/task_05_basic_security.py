from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
# Changez cela pour un secret plus fort
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Utilisateurs simulés en mémoire
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """ Vérifie les identifiants pour l'authentification basique """
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """ Route protégée par authentification basique """
    return "Basic Auth: Access Granted", 200  # Retourne du texte brut pour correspondre au test


@app.route('/login', methods=['POST'])
def login():
    """ Connexion et génération du token JWT """
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]['role']})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """ Route protégée par JWT """
    return "JWT Auth: Access Granted", 200  # Retourne du texte brut pour correspondre au test


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """ Route accessible uniquement aux admins """
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    # Retourne du texte brut pour correspondre au test
    return "Admin Access: Granted", 200

# Gestion des erreurs JWT


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run(debug=True)
