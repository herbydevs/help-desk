from flask import Blueprint, request, jsonify, session
import sqlite3

auth_bp = Blueprint('auth', __name__)

# Function to get a DB connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # This allows for column access by name
    return conn

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        # Connect to the database
        conn = get_db_connection()

        # Query for user by email
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if user:
            # Assuming password is stored in plain text at index 2
            stored_password = user['password']

            print(f"Stored password: {stored_password}")  # Debugging print
            print(f"Password entered: {password}")  # Debugging print

            # Check if the entered password matches the stored plain-text password
            if password == stored_password:
                # Store user info in session
                session['user'] = user['email']  # Use column name 'email'
                session['role'] = user['role']  # Use column name 'role'
                conn.close()
                return jsonify({'message': 'Logged in successfully', 'role': user['role']}), 200
            
            else:
                conn.close()
                return jsonify({'error': 'Invalid credentials'}), 401
        else:
            conn.close()
            return jsonify({'error': 'User not found'}), 404

    except sqlite3.Error as e:
        conn.close()
        return jsonify({'error': f'Database error: {str(e)}'}), 500
