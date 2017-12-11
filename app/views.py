#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import app
import requests
import simplejson
from flask import render_template
from flask import make_response
from flask import request
from flask import abort
from .form import TextFieldForm
from flask import url_for
from flask import redirect


@app.route('/')
def message():
    """ Simply prints "Hello World - Varshaa"  . Takes no arguments """

    message = 'Hello World - Varshaa'
    return render_template('message.html', message=message)


@app.route('/authors')
def authors():
    """ Hits the endpoint to get the json and deserializes the json
    to python object. The following collections are formed :
    1.dict_authors : author id -> author name
    2.dict_posts : author_id ->post_id
    3.temp_list : only author_id from dict_post
    4.dict_posts_count : user_id -> count by taking count of the user
    id's in the list.The data thus extracted is then renderes as html.
    """

    dict_authors = {}
    dict_posts = {}
    dict_posts_count = {}
    temp_list = []

    uri_authors_json = 'https://jsonplaceholder.typicode.com/users'
    uri_posts_json = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response_authors_json = requests.get(uri_authors_json)

        response_posts_json = requests.get(uri_posts_json)
    except requests.ConnectionError:
        return 'CONNECTION ERROR'
    response_authors_json_text = response_authors_json.text
    response_posts_json_text = response_posts_json.text

    authors_json = simplejson.loads(response_authors_json_text)
    posts_json = simplejson.loads(response_posts_json_text)
    for i in range(0, len(authors_json)):
        dict_authors[authors_json[i]['id']] = authors_json[i]['name']
    for j in range(0, len(posts_json)):
        dict_posts[posts_json[j]['id']] = posts_json[j]['userId']
    for (key, value) in list(dict_posts.items()):
        temp_list.append(dict_posts[key])
    for k in set(temp_list):
        dict_posts_count[k] = temp_list.count(k)

    return render_template('author.html', authors=dict_authors,
                           posts_count=dict_posts_count)


@app.route('/setcookie')
def set_cookie():
    """ Makes a response and checks if the cookies are already
    set. If not set, sets and returns them"""

    res = make_response(render_template('message.html',
                        message='Your cookies are being set'))
    if 'name' not in request.cookies:
        res.set_cookie('name', value='varshaa')
    if 'age' not in request.cookies:
        res.set_cookie('age', value='24')
    return res


@app.route('/getcookie')
def get_cookie():
    """ Gets the cookies and displays them"""

    name = request.cookies.get('name')
    age = request.cookies.get('age')
    return render_template('cookie.html', message_name=name,
                           message_age=age)


@app.route('/deny', methods=['GET', 'POST'])
def deny():
    """ Denies access to /deny endpoint"""

    abort(403)
    return render_template('message.html',
                           message='You dont have access to the requested page'
                           )


@app.route('/output', methods=['POST', 'GET'])
def output():
    """ If the method is post retrieves form data and displays the same """

    if request.method == 'POST':
        output = request.form['input_field']
    return render_template('output.html', value=output)


@app.route('/input', methods=['POST', 'GET'])
def input():
    """ Renders the form to be filled """

    form = TextFieldForm()
    return render_template('form.html', form=form)


@app.route('/image')
def image():
    """ Renders an image """

    return render_template('image.html')

			