from flask import Blueprint, request, jsonify, session
import sqlite3
from datetime import datetime

ticket_bp = Blueprint('ticket', __name__)

# Function to get a DB connection
def get_db_connection():
    conn = sqlite3.connect('tickets.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ticket submission route
@ticket_bp.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    # Get data from the request body
    data = request.json
    subject = data.get('subject')
    category = data.get('category')
    priority = data.get('priority')
    description = data.get('description')

    # Validate that all fields are provided
    if not all([subject, category, priority, description]):
        return jsonify({'error': 'All fields are required'}), 400

    try:
        # Connect to the database
        conn = get_db_connection()

        # Insert the ticket into the database
        conn.execute('''
            INSERT INTO tickets (subject, category, priority, description, submitted_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (subject, category, priority, description, datetime.now().isoformat()))

        # Commit and close the connection
        conn.commit()
        conn.close()

        # Return success message
        return jsonify({'message': 'Ticket submitted successfully'}), 200
    except sqlite3.Error as e:
        # Handle any database-related errors
        return jsonify({'error': f'Error saving ticket: {str(e)}'}), 500
 
@ticket_bp.route('/admin/tickets', methods=['GET'])
def get_tickets():
    try:
        # Connect to the database
        conn = get_db_connection()
        
        # Fetch all tickets from the database
        tickets = conn.execute('SELECT * FROM tickets').fetchall()

        # Convert the tickets to a list of dictionaries (one per row)
        ticket_list = []
        for ticket in tickets:
            ticket_list.append({
                'id': ticket['id'],
                'subject': ticket['subject'],
                'category': ticket['category'],
                'priority': ticket['priority'],
                'description': ticket['description'],
                'submitted_at': ticket['submitted_at']
            })

        # Close the connection
        conn.close()

        # Return the tickets in JSON format
        return jsonify(ticket_list), 200
    except sqlite3.Error as e:
        return jsonify({'error': f'Error fetching tickets: {str(e)}'}), 500
@ticket_bp.route('/tickets/<int:ticket_id>', methods=['PATCH'])
def update_ticket_status(ticket_id):
    try:
        data = request.get_json()
        new_status = data.get('status')

        conn = get_db_connection()
        cursor = conn.cursor()

        # Update the ticket status in the database
        cursor.execute('UPDATE tickets SET status = ? WHERE id = ?', (new_status, ticket_id))
        conn.commit()
        conn.close()

        return jsonify({'success': True}), 200
    except sqlite3.Error as e:
        return jsonify({'error': f'Error updating ticket: {str(e)}'}), 500


