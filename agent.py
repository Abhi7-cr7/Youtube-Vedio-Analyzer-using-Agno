#to run this script-> /usr/local/bin/python3 /Users/abhishekdesai/Documents/AgenticAI/agent.py

from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="you are helpful and expert travel agent.",
        add_datetime_to_context=True
    )
agent= build_agent()

agent.print_response("my budget is 1L INR, schould i travel to goa or phuket?")
