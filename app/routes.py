"""
routes.py
Route controls for website
"""
from app import app
from flask import render_template, request, redirect, url_for, jsonify
import string2words

@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
   print(request.args.get('input'))
   inputString = request.args.get('input')
   encodedWords = string2words.encode(inputString)
   return jsonify({'encoding':encodedWords})   

@app.route('/decode', methods=['GET', 'POST'])
def decode():
   print(request.args.get('input'))
   inputWords = request.args.get('input')
   inputWords = [int(i) for i in inputWords.split(',')]
   decodedString = string2words.decode(inputWords)
   return jsonify({'decoding':decodedString})  

@app.after_request
def add_header(r):
   r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
   r.headers["Pragma"] = "no-cache"
   r.headers["Expires"] = "0"
   r.headers['Cache-Control'] = 'public, max-age=0'
   return r
