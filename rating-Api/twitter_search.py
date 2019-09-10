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
import re
from nltk.stem.porter import * 
import nltk
import pandas as pd

class TwitterSearch(Resource):
    model = None
    tokenizer = None
    twitter_auth_data = None
    graph = None
    tweeter_api = None

    @classmethod
    def start(cls):
        # start
        TwitterSearch.model = load_model('best_model.hdf5')
        TwitterSearch.graph = tf.get_default_graph()
        TwitterSearch.tokenizer = TwitterSearch.tokenizer_full_text('full_text')
        TwitterSearch.twitter_auth_data = TwitterSearch.read_twitter_config('config.json')
        TwitterSearch.tweeter_api = TwitterSearch.get_twitter_api(TwitterSearch.twitter_auth_data)

    @classmethod
    def read_full_text(cls, filename):
        with open (filename, 'rb') as fp:
            full_text = pickle.load(fp)
            return full_text

    @classmethod
    def tokenizer_full_text(cls, filename):
        tk = Tokenizer(lower = True, filters='')
        stemmer = PorterStemmer()
        full_text_split = list(map(lambda x: x.split(), TwitterSearch.read_full_text(filename)))
        full_text = list(map(lambda x: [stemmer.stem(i) for i in x], full_text_split))
        tk.fit_on_texts(full_text)
        return tk

    @classmethod
    def read_twitter_config(cls, filename):
        with open(filename) as json_data_file:
            data = json.load(json_data_file)
            return data

    @classmethod
    def get_twitter_api(cls, twitter_auth_data):
        auth = tweepy.OAuthHandler(twitter_auth_data['consumer_key'], twitter_auth_data['consumer_secret'])
        auth.set_access_token(twitter_auth_data['access_token'], twitter_auth_data['access_token_secret'])
        api = tweepy.API(auth)
        return api
    
    @classmethod    
    def remove_pattern(cls, input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)
        return input_txt

    @classmethod
    def clean_tweets_text(cls, tweets):
        removed_mention_tweets = np.vectorize(TwitterSearch.remove_pattern)(tweets, "@[\w]*")
        series_removed_mention_tweets = pd.Series(removed_mention_tweets)
        series_removed_mention_tweets = series_removed_mention_tweets.astype(str)
        cleaned_tweets = series_removed_mention_tweets.replace("[^a-zA-Z’-]", " ")
        remove_short_words_cleaned_tweets = cleaned_tweets.apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
        tokenized_tweet = remove_short_words_cleaned_tweets.apply(lambda x: x.split())
        stemmer = PorterStemmer()
        stemmed_cleaned_tweets = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
        for i in range(len(stemmed_cleaned_tweets)):
            stemmed_cleaned_tweets[i] = ' '.join(stemmed_cleaned_tweets[i])
        stemmed_cleaned_tweets = stemmed_cleaned_tweets.astype(str)
        final_clean_tweets = TwitterSearch.tokenizer.texts_to_sequences(stemmed_cleaned_tweets.to_numpy())
        max_len = 50
        tweets_padded = pad_sequences(final_clean_tweets, maxlen = max_len)
        return tweets_padded

    def get(self, search_keyword, count):
        if TwitterSearch.tweeter_api is None:
            TwitterSearch.start()
        count = int(count)
        result = []
        full_tweets = []
        for tweet in tweepy.Cursor(TwitterSearch.tweeter_api.search, q=search_keyword, lang='en', tweet_mode='extended').items(count):
            result.append(tweet.full_text)
            full_tweets.append(tweet._json)
        cleaned_result = TwitterSearch.clean_tweets_text(result)
        global graph
        with TwitterSearch.graph.as_default():
            pred = TwitterSearch.model.predict(cleaned_result)
        if len(pred) == 0:
            predictions = []
        else:
            predictions = np.round(np.argmax(pred, axis=1)).astype(int)
            predictions = predictions.tolist()
        return_result = []
        for i in range(len(full_tweets)):
            return_result.append((full_tweets[i], predictions[i]))
        return jsonify(return_result)
