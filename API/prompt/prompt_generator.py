from api.openai import OpenAIAPI


class PromptGenerator:
    def __init__(self):
        self.api = OpenAIAPI()
    @property
    def brand_context_template(self):
        return """Insight: {insight}
        Vision: {vision}
        Mission: {mission}
        Solution: {solution}
        Values: {values}
        Target audience: {target_audience}
        Personality: {personality}
        Tone of voice: {tone_of_voice}
        Characteristics: {characteristics}
        Communication pillars: {communication_pillars}
        """

    def generate_brand_context_response(self, human_template, input_parameters):
        input_parameters = {
            "insight": "Followers of the president are happy that the president is already someone who represents the country so none has to be ashamed.",
            "vision": "I want to make Czech republic ambitious and confident country where the people want to live in.",
            "mission": "By representing our country with dignity and also by using the authority and possibilities of the head of state to promote important topics and solutions that will move our country in the right direction.",
            "solution": "Listening to people, prudent decisions, respect for opponents, friendly attitude, respected personality at the international level.",
            "values": "independence, fair-play, transparent, empathy, respect, good will",
            "target_audience": "men & women in the age between 20 - 40 years old, who are following the president for the emotional and personal reasons",
            "personality": "He is competent - reliable, efficient, and effective. Often associated with qualities such as intelligence, professionalism, and expertise.",
            "tone_of_voice": "formal, deliberate, respectful, matter-of-fact",
            "characteristics": "Trustworthy, professional, pragmatic, smart, patient, conventional",
            "communication_pillars": "politics, presidential agenda, motivational speeches"
        } if input_parameters is None else input_parameters
        return self.api.chat_prompt_response(system_template=self.brand_context_template, human_template=human_template, **input_parameters)

    def generate_analysis_response(self, human_template, posts):
        joined_posts = ".\n".join(posts)
        analysis_template = """
        Posts: 
        {joined_posts}    
        """
        return self.api.chat_prompt_response(system_template=analysis_template, human_template=human_template, joined_posts=joined_posts)

