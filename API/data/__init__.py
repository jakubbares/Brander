import os
import json
DATA_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FACEBOOK_POSTS_PATH = os.path.join(DATA_DIRECTORY, "FB_posts_CZ.json")
TEST_PROMPT_FULL_PATH = os.path.join(DATA_DIRECTORY, "test_prompt.txt")


FACEBOOK_POSTS = json.load(open(FACEBOOK_POSTS_PATH, 'r'))
TEST_PROMPT_FULL = open(TEST_PROMPT_FULL_PATH, 'r').read()

TEST_PROMPT_HUMAN = """
Hey, try to imagine you are the president of the Czech Republic Petr Pavel and you visited mc'donald where you have ordered the Big Mac which was very tasty. Now you are writing the post about it on Instagram. The post length is 50 words. Write it according to all these specifications but do not express them explicitly. Just act accordingly:
"""
