from flask import Flask
from flask import g
from flask_restful import Api
from flask_cors import CORS

import os

from openai_api.langchain import OpenAIAPI

os.environ["OPENAI_API_KEY"] = "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"

from common.logger import Logger
from endpoints.input import InputCollector


logger = Logger().logger

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/brander/*": {"origins": "*"}})

api.add_resource(InputCollector, '/brander/input')


if __name__ == "__main__":
    logger.info('###############################')
    logger.info('##  Running Brander - API ######')
    logger.info('###############################')

    app.run(host='0.0.0.0', port=5000)


