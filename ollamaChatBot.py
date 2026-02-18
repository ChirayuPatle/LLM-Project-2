import os
import streamlit as st

# import python build in os tools
from langchain_community.llms import ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import strOutParser

# Step 1 : create project template
# Define how AI behaves and how user recieves user input 

prompt = ChatPromptTemplate.from_messages(
    {
        # system messages define AI behaviour
        ("system","you are a helpful assistant. please respomt clearly to the questions asked."),

        # user message contains placeholder{question}
        ("user","Question: {question}")
    }
)

# Step 2 : streamlit app UI

st.set_page_config(
    page_title="Mini AI App",
    page_icon="",
    layout="centered"
)

st.title("Mini AI Assistant")
st.write("This is a simple Streamlit UI example.")


st.sidebar.header("Settings")
temperature = st.sidebar.slider("Creativity Level", 0.0, 1.0, 0.5)

user_input = st.text_input("Ask something:")

if st.button("Generate Response"):
    if user_input:
        st.success("Response Generated!")
        st.write(f"**You asked:** {user_input}")
        st.write(f"**Creativity Level:** {temperature}")
        st.info("This is a demo response from your mini AI app.")
    else:
        st.warning("Please enter a question first!")

st.markdown("---")
st.caption("Built with using Streamlit")


# Step 3 : load ollama model

# load local gemma model
LLM = ollama(model="gemma2:2b")
