import json
from json import dumps
from flask import jsonify
from flask_restful import Resource, Api
import tweepy
import pickle
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, load_model
import numpy as np

class TwitterSearch(Resource):
    model = None
    tokenizer = None
    twitter_auth_data = None
    graph = None

    @classmethod
    def start(cls):
        # start 
        TwitterSearch.model = load_model('best_model.hdf5')
        TwitterSearch.graph = tf.get_default_graph()
        TwitterSearch.tokenizer = TwitterSearch.tokenizer_full_text('full_text')
        TwitterSearch.twitter_auth_data = TwitterSearch.read_twitter_config('config.json')


    @classmethod
    def read_full_text(cls, filename):
        with open (filename, 'rb') as fp:
            full_text = pickle.load(fp)
            return full_text

    @classmethod
    def tokenizer_full_text(cls, filename):
        tk = Tokenizer(lower = True, filters='')
        tk.fit_on_texts(TwitterSearch.read_full_text(filename))
        return tk

    @classmethod
    def read_twitter_config(cls, filename):
        with open(filename) as json_data_file:
            data = json.load(json_data_file)
            return data

    def get(self, search_keyword, count):
        print("here")
        print(TwitterSearch.twitter_auth_data['consumer_key'])
        print(TwitterSearch.model)
        print("end")
        count = int(count)
        auth = tweepy.OAuthHandler(TwitterSearch.twitter_auth_data['consumer_key'], TwitterSearch.twitter_auth_data['consumer_secret'])
        auth.set_access_token(TwitterSearch.twitter_auth_data['access_token'], TwitterSearch.twitter_auth_data['access_token_secret'])
        api = tweepy.API(auth)
        result = []
        for tweet in tweepy.Cursor(api.search, q=search_keyword).items(count):
            result.append(tweet.text)
        result_tokenized = TwitterSearch.tokenizer.texts_to_sequences(result)
        max_len = 50
        pad_result = pad_sequences(result_tokenized, maxlen = max_len)
        #return jsonify(pad_result.tolist())
        global graph
        with TwitterSearch.graph.as_default():
            pred = TwitterSearch.model.predict(pad_result)
        predictions = np.round(np.argmax(pred, axis=1)).astype(int)
        predictions = predictions.tolist()
        return_result = []
        for i in range(len(result)):
            return_result.append((result[i], predictions[i]))
        return jsonify(return_result)
