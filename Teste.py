# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message # type: ignore
import hashlib
import os
import _sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'maribragad@gmail.com'
app.config['MAIL_PASSWORD'] = 'mqgo oiaf qgwn efjw'
app.config['MAIL_DEFAULT_SENDER'] = 'maribragad@gmail.com'
mail = Mail(app)

# Dummy user database
users = {
    'user1': {'email': 'maribragad@gmail.com', 'password': 'password1'},
    'user2': {'email': '2100760@aluno.univesp.br', 'password': 'password1'}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def forgot_password():
    email = request.form['email']
    if email in [user['email'] for user in users.values()]:
    # Rest of the code

        # Generate a hash for the email
        hash_value = hashlib.sha256(email.encode()).hexdigest()

        # Send the hash to the user's email
        msg = Message('Password Reset', recipients=[email])
        msg.body = f"Please use the following hash to reset your password: {hash_value}"
        mail.send(msg)

        flash('Password reset link sent to your email.')
        return redirect(url_for('login'))
    else:
        flash('Email not found in our records.')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)