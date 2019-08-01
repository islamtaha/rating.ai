from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json
from json import dumps
from flask import jsonify
import tweepy
from twitter_search import TwitterSearch

app = Flask(__name__)
api = Api(app)

api.add_resource(TwitterSearch, '/twitter/<search_keyword>') # Route_3

if __name__ == '__main__':
     app.run(port='5002')
     