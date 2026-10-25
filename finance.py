from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools(),YFinanceTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["use given tools whenever possible,Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )
agent= build_agent()

agent.print_response("Share the NVDA stock price and analyst recommendations and analyst recommendation")