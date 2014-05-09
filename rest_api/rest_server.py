#!env/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
words = dict()

# Since we're an API sending back a bunch of HTML is wrong, this fixes that.
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)

# Just for silly
@app.route('/')
def index():
	return "Nothing to see here, move long!"

# This returns all words and their counts as JSON
@app.route('/words', methods = ['GET'])
def get_words():
	if words == dict():
		return jsonify( { "error": "No data entered yet." } ), 400
	return jsonify( { 'words': words } )

# This returns a single word and its count as JSON
@app.route('/words/<word>', methods = ['GET'])
def get_word(word):
	try:
		count = words[word]
	except KeyError:
		return jsonify( { "error": "No such word: {w}".format(w=word) } ), 400

	return jsonify( { word: count } )

# This is how words are added. JSON should be: { "word": "ONE_WORD" }
@app.route('/word', methods = ['PUT'])
def add_word():
	if not request.json:
		return jsonify( { "error": "Request not set to application/json" } ), 400

	try:
		word = request.json["word"]
	except:
		return jsonify( { "error": "malformed JSON, only 'word' is allowed" } ), 400

	if len(word.split()) != 1:
		return jsonify( { "error": "PUT requests must be one word in length" } ), 400

	try:
		words[word] += 1
	except KeyError:
		words[word] = 1

	return jsonify( { 'word': word, "count": words[word] } )

if __name__ == '__main__':
	app.run(debug = True)
