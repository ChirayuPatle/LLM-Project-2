import os
import streamlit as st

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# step1: create prompt template
# this defin how ai should behave and how it recieves user input

prompt = ChatPromptTemplate.from_messages(
    {
        #system messages define AI behaviour
        ("system","you are a helpful assistant. please respomt clearly to the questions asked."),
        #user message contains placeholder{question}
        ("user","Question: {question}")
    }
)

#step 2: stream app ui

#App title
st.title("langchain demo with gemma model(ollama)")

#text input box for user input question
input_txt = st.text_input("What question do you have in your mind?")

#step 3: load ollama model

#load local gemma model
LLM = Ollama(model="gemma2:2b")

#condition-convert output model to string

output_parser = StrOutputParser()

#create langchain pipeline (prompt --> model --> output_parser)
chain = prompt | LLM | output_parser

#step4: run the model when user inputs the question
if input_txt:
    response = chain.invoke({"question":input_txt})
    st.write(response)