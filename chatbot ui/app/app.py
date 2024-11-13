import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize LangChain components
llm = Ollama(model="llama3.2")

# Define the chatbot's prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical documentation writer specializing in computer science topics."),
    ("user", "{input}")
])

# Combine the prompt, model, and output parser
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit app interface
st.title("Computer Science Chatbot")
st.write("Ask any computer science-related question!")

# User input
user_input = st.text_input("Enter your question:")

if user_input:
    # Invoke the LangChain chain with user input
    response = chain.invoke({"input": user_input})
    # Display the response
    st.write("Chatbot response:")
    st.write(response)
