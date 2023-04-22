import json

from data import FACEBOOK_POSTS
from prompt.prompt_generator import PromptGenerator


class PostAnalysis:
    def __init__(self):
        self.generator = PromptGenerator()
        self.posts = FACEBOOK_POSTS.values()
        self.human_template = """
        Extrahuj klíčová témata z textů. Představ si, že jsi žurnalista. 
        Jak by jsi definoval témata, která jsou nejsilnější v těchto postech? 
        Vrať jako array témat ve formátu JSON.
        """

    def process(self):
        topics = self.extract_topics()
        print(topics)

    def extract_topics(self):
        return self.generator.generate_analysis_response(human_template=self.human_template, posts=self.posts)

