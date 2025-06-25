from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

#register blueprints
from routes.main import main
from routes.contact import contact
from routes.factory import factory
from routes.product import product
from routes.services import services  
from routes.profile import profile  

app.register_blueprint(main)
app.register_blueprint(contact)
app.register_blueprint(factory)
app.register_blueprint(product)
app.register_blueprint(services)
app.register_blueprint(profile)  

if __name__ == "__main__":
    app.run(debug=True)
# This file is the entry point for the Flask application.
# It initializes the app, configures Flask-Mail, and registers the blueprints.