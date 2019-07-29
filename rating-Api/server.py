from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

app = Flask(__name__)
api = Api(app)

class TwitterSearch(Resource):
    def get(self, search_keyword):
        result = {'data': "result "+ search_keyword}
        return jsonify(result)
        

api.add_resource(TwitterSearch, '/twitter/<search_keyword>') # Route_3

if __name__ == '__main__':
     app.run(port='5002')
     