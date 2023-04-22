from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from typing import List, Dict


class OpenAIAPI:
    def __init__(self):
        self.llm = OpenAI(temperature=0.9)
        self.chat_model = ChatOpenAI(temperature=0)

    def basic_prompt_response(self, prompt: str):
        return self.llm(prompt)

    def formatted_prompt_response(self, prompt: PromptTemplate, **inputs):
        chain = LLMChain(llm=self.llm, prompt=prompt)
        chain.run(**inputs)

    def chat_prompt_response(self, system_template: str, human_template: str, **inputs):
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        chain = LLMChain(llm=self.chat_model, prompt=chat_prompt)
        return chain.run(**inputs)
