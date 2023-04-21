from flask import Flask
from flask import g
from flask_restful import Api
from flask_cors import CORS

from common.logger import Logger
from endpoints.configuration import Configuration


logger = Logger().logger

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/brander/*": {"origins": "*"}})

api.add_resource(Configuration, '/brander/api')


if __name__ == "__main__":
    logger.info('###############################')
    logger.info('##  Running Brander - API ######')
    logger.info('###############################')

    app.run(host='0.0.0.0', port=3400)
