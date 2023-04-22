import json

from flask import jsonify
from flask_restful import Resource, reqparse

from prompt.post_analysis import PostAnalysis
from prompt.prompt_generator import PromptGenerator


class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': "fuck"}



class ContentStrategy(Resource):
    def __init__(self):
        self.generator = PromptGenerator()
        self.analysis = PostAnalysis()
        self.parameters = {}
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('input_parameters_json', type=json, required=False, help='Input parameters', default=None, location="json")
        self.parser.add_argument('human_template', type=str, required=False, help='Human template cannot be blank', location="json")
        super(ContentStrategy, self).__init__()

    def get(self):
        item = {
            'id': 1,
            'name': 'Example item',
            'price': 9.99,
        }
        return jsonify(item)
    def post(self):
        args = self.parser.parse_args()
        # Do something with the arguments (e.g., authenticate the user)
        input_parameters = args['input_parameters_json'] if args['input_parameters_json'] else {}
        analysis = self.analysis.process()
        parameters = {**input_parameters, **analysis}
        print(parameters)
        #TODO Add self.paramters to function below
        print("////")
        print(args["human_template"])
        print("////")
        response = self.generator.generate_brand_context_response(input_parameters=input_parameters, human_template=args["human_template"])
        print(response)
        return jsonify({"response": response})
