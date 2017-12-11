#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')


class TextFieldForm(Form):

    input_field = StringField('Enter text here',
                              validators=[DataRequired()])