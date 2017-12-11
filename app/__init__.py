from flask import Flask
from flask import render_template
import requests
import simplejson

app = Flask(__name__)
app.config.from_object('config')

from app import views
