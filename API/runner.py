from langchain import PromptTemplate

from openai_api.langchain import OpenAIAPI
import os


os.environ["OPENAI_API_KEY"] = "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"


api  = OpenAIAPI()
res = api.basic_prompt_response("What is a good name for a company that makes Coke?")
print(res)


prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
res = api.formatted_prompt_response(prompt=prompt, product="Coke")
print(res)


res = api.chat_prompt_response(system_template="You are a helpful assistant that translates {input_language} to {output_language}.",
                               human_template="{text}",
                               input_language="English", output_language="French", text="I love programming."
)
