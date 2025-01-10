import os
import streamlit as st


from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI  # Updated import for chat models

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature = 0.8, openai_api_key = os.getenv("OPENAI_API_KEY"), model_name = "gpt-3.5-turbo")

def humanizer(input):
    
    Prompt = """
    You are an expert at transforming AI-generated text into natural, human-like language 
    that feels conversational and engaging. Your task is to take AI-generated content and 
    rewrite it in a way that is 100 percentage humanized. The final output should be clear, 
    expressive, and free from robotic or overly formal tones, while preserving the original
    meaning and intent.

     Here’s the content to humanize:

    AI-Generated Text: {input}
    Please provide:

    A rewritten version that feels natural and human-like."""
    
    humanize_prompt = PromptTemplate(
        input_variables = ["input"],
        template = Prompt
    )
    
    chain1 = LLMChain(
        llm = llm,
        prompt = humanize_prompt
    )
    
    return chain1.run({"input" : input})



def summerizer(input):
    prompt_text = """
    You are an expert text summarizer with the ability to condense long pieces of text into clear, concise, and meaningful summaries. 
    Your task is to take the provided content and rewrite it in a way that captures the essential points while preserving the original 
    meaning and intent. The summary should be easy to understand, free from unnecessary details, and suitable for quick reading.

    Here’s the content to summarize:

    Original Text: {input}
    
    Please provide:

    A summary that highlights the key points and main ideas.
    """
    
    summerize = PromptTemplate(
        input_variables = ["input"],
        template = prompt_text
    )
    
    chain2 = LLMChain(
        llm = llm,
        prompt = summerize
    )
    
    return chain2.run({"input" : input})

def grammer_checker(input):
    prompt_text = """
    You are an advanced AI grammar checker with the capability to analyze text for grammatical accuracy. 
    Your task is to review the provided content, correct any grammatical mistakes, and deliver a refined version of the text with perfect grammar.

    Here's the content to analyze:

    Text to Analyze: {input}
    
    Please provide:

    1. The corrected version of the text with no grammatical errors.
    """ 
 
    
    detector = PromptTemplate(
        input_variables = ["input"],
        template = prompt_text
    )
    
    chain3 = LLMChain(
        llm = llm, 
        prompt = detector
    )
    
    return chain3.run({"input":input})

st.set_page_config(page_title="P75")

st.header("P75")


input = st.text_area("What can I help with? ",key = "input", height=225)


col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button("Humanizer")

with col2:
    button2 = st.button("Text Summerizer")
    
with col3:
    button3 = st.button("Grammer Checker")
    
if button1:
    response = humanizer(input)
    st.subheader("Humanized Data")
    st.write(response)

if button2:
    response = summerizer(input)
    st.subheader("Summerized Data")
    st.write(response)

if button3:
    response = grammer_checker(input)
    st.subheader("AI Detector")
    st.write(response)