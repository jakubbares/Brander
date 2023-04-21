from flask_restful import Resource, reqparse
from common.logger import Logger
logger = Logger().logger

class PromptExtender(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('prompt', required=True, location='json', type=str)
        args = parser.parse_args()

