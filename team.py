from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

eng_agent=Agent(name="English Agent", role="You answer questions in English")
chinese_agent=Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_agent=Agent(name="Hindi Agent", role="You answer questions in hindi")

team_leader= Team(
    name="Multilingual Agent Team",
    members=[eng_agent,chinese_agent,hindi_agent],
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must respond to the answer query in their specific language
                    Do not call just one agent.
                    output the response of all agents.    
                """
)

team_leader.print_response("what is the capitcal of India?")