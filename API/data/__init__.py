import os
import json
DATA_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FACEBOOK_POSTS_PATH = os.path.join(DATA_DIRECTORY, "FB_posts_CZ.json")
TEST_PROMPT_FULL_PATH = os.path.join(DATA_DIRECTORY, "test_prompt.txt")


#FACEBOOK_POSTS = json.load(open(FACEBOOK_POSTS_PATH, 'r'))
#TEST_PROMPT_FULL = open(TEST_PROMPT_FULL_PATH, 'r').read()

TEST_PROMPT_HUMAN = """
Hey, try to imagine you are the president of the Czech Republic Petr Pavel and you visited mc'donald where you have ordered the Big Mac which was very tasty. Now you are writing the post about it on Instagram. The post length is 50 words. Write it according to all these specifications but do not express them explicitly. Just act accordingly:
"""

TEST_PROMPT_FULL = """
Hey, try to imagine you are the president of the Czech Republic Petr Pavel and you visited mc'donald where you have ordered the Big Mac which was very tasty. Now you are writing the post about it on Instagram. The post length is 50 words. Write it according to all these specifications but do not express them explicitly. Just act accordingly:

Insight: Followers of the president are happy that the president is already someone who represents the country so none has to be ashamed.

Vision: I want to make Czech republic ambitious and confident country where the people want to live in.

Mission: By representing our country with dignity and also by using the authority and possibilities of the head of state to promote important topics and solutions that will move our country in the right direction.

Solution: Listening to people, prudent decisions, respect for opponents, friendly attitude, respected personality at the international level.

Values: independence, fair-play, transparent, empathy, respect, good will

Target audience: men & women in the age between 20 - 40 years old, who are following the president for the emotional and personal reasons

Personality: He is competent - reliable, efficient, and effective. Often associated with qualities such as intelligence, professionalism, and expertise.

Tone of voice: formal, deliberate, respectful, matter-of-fact,

Characteristics: Trustworthy, professional, pragmatic, smart, patient, conventional

Communication pillars: politics, presidential agenda, motivational speeches

Translate it to Czech

"""
