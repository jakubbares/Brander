from flask_restful import Resource, reqparse
from common.logger import Logger
logger = Logger().logger


class PromptExtender(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('prompt', required=True, location='json', type=str)
        args = parser.parse_args()


        result = comparator.compare_two_sentences(userText, args.get('generated'), RuleEvaluator(["similarity-config-en.yaml"]))

        errors_txt = ""
        if len(result.errors) > 0:
            errors_txt = (_(result.errors)
                          .map(lambda a: a.to_string())
                          .reduce(lambda a, b: a + " " + b)
                          ._)
        print("score:{} errors:{}".format(result.overall_score, errors_txt))
        return {"score": result.overall_score, "detail": errors_txt}, 200

