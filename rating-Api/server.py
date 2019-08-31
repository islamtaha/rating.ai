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
    TwitterSearch.start()
    app.run(port='5002')
     