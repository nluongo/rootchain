import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatGoogleGenerativeAI(model='gemini-pro')

prompt = ChatPromptTemplate.from_template('tell me a short joke about {topic}')

output_parser = StrOutputParser()

chain = prompt | model | output_parser

print(chain.invoke({'topic': 'ice cream'}))
