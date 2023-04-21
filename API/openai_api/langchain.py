from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import List

class OpenAIAPI:
    def __init__(self):
        self.llm = OpenAI(temperature=0.9)
    def basic_prompt_response(self, prompt: str):
        return self.llm(prompt)

    def formatted_prompt_response(self, prompt: PromptTemplate, inputs: List[str]):
        chain = LLMChain(llm=self.llm, prompt=prompt)
        chain.run(inputs)


