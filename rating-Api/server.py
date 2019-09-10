import os
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json
from json import dumps
from flask import jsonify
import tweepy
from twitter_search import TwitterSearch
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

api.add_resource(TwitterSearch, '/twitter/<search_keyword>/<count>') # Route_3

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)