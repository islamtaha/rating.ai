import json
from json import dumps
from flask import jsonify
from flask_restful import Resource, Api
import tweepy

class TwitterSearch(Resource):
    
    def read_twitter_config(self, filename):
        with open(filename) as json_data_file:
            data = json.load(json_data_file)
            return data

    def get(self, search_keyword):
        twitter_auth_data = self.read_twitter_config("config.json")
        print(twitter_auth_data)
        auth = tweepy.OAuthHandler(twitter_auth_data['consumer_key'], twitter_auth_data['consumer_secret'])
        auth.set_access_token(twitter_auth_data['access_token'], twitter_auth_data['access_token_secret'])
        api = tweepy.API(auth)
        result = []
        for tweet in tweepy.Cursor(api.search, q=search_keyword).items(10):
            result.append(tweet.text)
        return jsonify(result)
