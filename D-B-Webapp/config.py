"""Flask config."""
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env")) #set environment variables in local file to make it cleaner


class Config:
    """Flask configuration variables."""
    #setting different configuration values depending on which enviroment we are running in

    # General Config
    FLASK_APP = environ.get("FLASK_APP") #flask app
    FLASK_ENV = environ.get("FLASK_ENV") #environment the app is running in 
    SECRET_KEY = environ.get("SECRET_KEY") #random strings used to encrypt sensitive user data

    # Assets
    LESS_BIN = environ.get("LESS_BIN")  #get less_bin asset
    ASSETS_DEBUG = environ.get("ASSETS_DEBUG") #enable debugger for static assets
    LESS_RUN_IN_DEBUG = environ.get("LESS_RUN_IN_DEBUG") #enable less_bin debugger

    # Static Assets
    STATIC_FOLDER = "static" #access static folder
    TEMPLATES_FOLDER = "templates" #access templates folder
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG") #enable debugger for asset compressor
