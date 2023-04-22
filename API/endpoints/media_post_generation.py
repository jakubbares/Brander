import json
from flask import jsonify
from flask_restful import Resource, reqparse

from prompt.post_analysis import PostAnalysis
from prompt.prompt_generator import PromptGenerator


class MediaPostGeneration(Resource):
    def __init__(self):
        self.analysis = PostAnalysis()
        self.generator = PromptGenerator()
        self.parameters = {}

    def post(self):
        # Parse the arguments from the request using reqparse
        parser = reqparse.RequestParser()
        parser.add_argument('human_template', type=str, required=True, help='Username cannot be blank')
        parser.add_argument('input_parameters_json', type=str, required=True, help='Username cannot be blank')
        args = parser.parse_args()
        input_parameters = json.loads(args['input_parameters_json'])
        analysis = self.analysis.process()
        self.parameters = {**input_parameters, **analysis}
        response = self.generator.generate_brand_context_response(input_parameters=self.parameters, human_template=args["human_template"])
        print(response)
        return jsonify({"response": response})


