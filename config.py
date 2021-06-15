import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.getenv('SQLALCHEMY_DATABASE_URI').startswith('postgres'):
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    # MAIL_SERVER = pass #create sendgrid.net
    # MAIL_PORT = pass #create mail port from sendgrid
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    ADMINS = ['felixlopmsc@gmail.com']
    ITEMS_PER_PAGE = 8