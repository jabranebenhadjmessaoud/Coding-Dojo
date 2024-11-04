from flask import Flask,flash


app=Flask(__name__)
app.secret_key="password123"
DB="email_validation_schema"