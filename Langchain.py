#!/usr/bin/env python
from typing import List


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from flask import Flask,jsonify
import os
from dotenv import load_dotenv  

load_dotenv()

app = Flask(__name__)
# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI(openai_api_key = os.environ['OPENAI_API_KEY'])

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


@app.route('/')
def home():
   return 'Welcome Home'

@app.route('/lang')
def msg_request():
    msg =chain.invoke({"language": "italian", "text": "What is your name"})
    return jsonify({'translation': msg})
    
    
if __name__ == "__main__":
    app.run()