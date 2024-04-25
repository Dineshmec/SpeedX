from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import Celery


app = Flask(__name__)
CORS(app,origins='http://127.0.0.1:5500')

# Celery configuration updated to new format
app.config['broker_url'] = 'redis://localhost:6379/0'
app.config['result_backend'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['broker_url'])
celery.conf.update(app.config)


# MySQL configurations
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='test_db'
)


# Generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))
 
# Send OTP to the specified email address
def send_otp(email, otp):
    sender_email = "oipmakeyourown@gmail.com"  # Your email address
    sender_password = "vvrd tais gzrz krqf"  # Your email password
    subject = "OTP for verification"
    message = f"Your OTP for verification is: {otp}"
 
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
 
    msg.attach(MIMEText(message, 'plain'))
 
    try:
       
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, email, text)
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", str(e))
        return False
 
@app.route('/send_otp', methods=['POST'])
def send_otp_route():
    cursor = db.cursor()
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email address not provided'}), 400
 
    otp = generate_otp()
    if send_otp(email, otp):
        cursor.execute("INSERT INTO otp (otp_value, used,email) VALUES (%s, %s,%s)", (otp,0,email))
        db.commit()
        return jsonify({'message': 'OTP sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send OTP'}), 500

@app.route('/login', methods=['POST'])
def login():
    cursor = db.cursor(dictionary=True)  # Ensure dictionary=True for fetching results as dictionaries

    # Get email and password from the request
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Query the database to check if the user exists
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {str(err)}'}), 500

    # If user is not found or password doesn't match, return error
    if not user or user['password'] != password:
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

# Endpoint for updating password
@app.route('/update_password', methods=['POST'])
def update_password():
    cursor = db.cursor()

    email = request.json.get('email')
    new_password = request.json.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required'}), 400

    # Update the password in the database
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
    db.commit()

    return jsonify({'message': 'Password updated successfully'}), 200

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()  # Get data as JSON
    email = data.get('email')
    
    if email:
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            db.commit()
            if result:
                return jsonify({'exists': True}), 200  # Email exists
            else:
                return jsonify({'exists': False}), 404  # Email not found
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Internal server error
    else:
        return jsonify({'error': 'Email parameter is missing'}), 400  # Bad request



# Endpoint for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    cursor = db.cursor()
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the user already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        return jsonify({'error': 'User already exists'}), 400

    # Add the new user to the database
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    db.commit()

    return jsonify({'message': 'User added successfully'}), 200


# API endpoint to validate OTP
@app.route('/validate_otp', methods=['POST'])
def validate_otp():
    data = request.json
    otp = data.get('otp')
    email = request.json.get('email')
    password = request.json.get('password')

    if not otp:
        return jsonify({'error': 'OTP not provided'}), 400

    # Connect to MySQL database
    try:
        cursor = db.cursor()

        # Check if the OTP exists in the database and is not already used
        query = "SELECT * FROM otp WHERE otp_value = %s AND used = FALSE AND email = %s"
        cursor.execute(query, (otp,email))
        otp_entry = cursor.fetchone()

        if otp_entry:
            # Mark the OTP as used
            update_query = "UPDATE otp SET used = TRUE WHERE id = %s"
            cursor.execute(update_query, (otp_entry[0],))  # Assuming id is the first column
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            db.commit()
            return jsonify({'message': 'OTP is valid'}), 200

        else:
            return jsonify({'error': 'Invalid OTP or OTP already used'}), 400

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error accessing database: {str(e)}'}), 500
    

if __name__ == '__main__':
    app.run(debug=True,port=5505)
