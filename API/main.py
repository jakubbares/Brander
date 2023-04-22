from flask import Flask, jsonify
from flask import g
from flask_restful import Api, Resource, marshal, reqparse
from flask_cors import CORS

import os

from common.logger import Logger
from endpoints.content_strategy import ContentStrategy
from endpoints.media_post_generation import MediaPostGeneration


logger = Logger().logger

app = Flask(__name__, static_url_path="")
api = Api(app)
cors = CORS(app, resources={r"/brander/*": {"origins": "*"}})

api.add_resource(MediaPostGeneration, '/brander/post', endpoint='post')
api.add_resource(ContentStrategy, '/brander/content_strategy', endpoint='content_strategy')



if __name__ == "__main__":
    logger.info('###############################')
    logger.info('##  Running Brander - API ######')
    logger.info('###############################')

    app.run(host='0.0.0.0', port=5000, debug=True)


