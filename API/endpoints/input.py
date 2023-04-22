import json

from flask_restful import Resource, reqparse

from prompt.post_analysis import PostAnalysis
from prompt.prompt_generator import PromptGenerator


class InputCollector(Resource):
    def __init__(self):
        self.generator = PromptGenerator()
        self.analysis = PostAnalysis()
        self.parameters = {}

    def generate_content_strategy(self):
        human_template = "Hey, try to imagine you are the president of the Czech Republic Petr Pavel and you visited mc'donald where you have ordered the Big Mac which was very tasty. Now you are writing the post about it on Instagram. The post length is 50 words. Write it according to all these specifications but do not express them explicitly. Just act accordingly"
        # Parse the arguments from the request using reqparse
        parser = reqparse.RequestParser()
        parser.add_argument('input_parameters_json', type=str, required=True, help='Username cannot be blank')
        parser.add_argument('human_template', type=str, required=True, help='Username cannot be blank')
        args = parser.parse_args()

        # Do something with the arguments (e.g., authenticate the user)
        input_parameters = json.loads(args['input_parameters_json'])
        analysis = self.analysis.process()
        self.parameters = {**input_parameters, **analysis}
        return {"response": self.generator.generate_brand_context_response(input_parameters=self.parameters, human_template=human_template)}

    def generate_media_post(self):
        # Parse the arguments from the request using reqparse
        parser = reqparse.RequestParser()
        parser.add_argument('human_template', type=str, required=True, help='Username cannot be blank')
        args = parser.parse_args()
        return {"response": self.generator.generate_brand_context_response(input_parameters=self.parameters, human_template=args["human_template"])}
