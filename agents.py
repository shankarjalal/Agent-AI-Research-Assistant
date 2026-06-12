# Import Libraries

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# Model setup
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0, max_retries=5)

# 1st agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )


# Write Chain (using runables)

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reprot."),
    ("human", """ Write a detailed research report on the topic below.
    
Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well - explained points)
- Conclusion
- Sources (list all URLs found in the research.)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic_Chain

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and secific"),
    ("human", """Review the research  below and evaluate it striclly.
    
Reprot:
{report}

Respond in this exact format:

Score: X/10

Strangths:
- ...
- ...

Area to Improve:
- ...
- ...

One Line verdict

    """)
])

critic_chain = critic_prompt | llm | StrOutputParser()

