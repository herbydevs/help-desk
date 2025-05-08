from flask import Flask
from auth import auth_bp  # Import auth blueprint
from tickets import ticket_bp
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

# Enable CORS for the frontend to communicate with the API
CORS(app, origins="http://localhost:5173", supports_credentials=True)

# Secret key for session management
app.secret_key = '123'

# Register the blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(ticket_bp)

@app.route('/')
def index():
    return {'message': 'Help Desk API is running'}

# Database helper function to connect to SQLite
def get_db_connection():
    conn = sqlite3.connect('helpdesk.db')
    conn.row_factory = sqlite3.Row  # This allows us to access rows as dictionaries
    return conn

if __name__ == '__main__':
    app.run(debug=True)
