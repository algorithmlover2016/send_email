from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email from environment
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your email password or app-specific password from environment

mail = Mail(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit-email', methods=['POST'])
def submit_email():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        msg = Message('Hello!', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
        msg.body = f"Hello, {email}!"
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)