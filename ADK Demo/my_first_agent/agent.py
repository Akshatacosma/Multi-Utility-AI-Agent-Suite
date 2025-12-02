from google.adk.agents import Agent
from google.adk.tools import google_search

def evening_greet(name: str) -> dict:
    return {"greeting": f"Good evening, {name}. 🌙 I hope you had a peaceful day."}

def morning_greet(name: str) -> dict:
    return {"greeting": f"Good morning, {name}! ☀️ Wishing you a productive day ahead."}

root_agent = Agent(
    name = "my_first_agent",
    model = "gemini-2.0-flash",
    description="An example agent that will answer user queries based on Google Search results and greet users based on the time of day.",
    instruction="""
    First Ask User a Name & Start conversation by greeting user with Name.You are AI Assistant that helps users with Google Cloud related queries.based on Google Search results.
    if user says Good Morning, use morning_greet tool to greet user.
    if user says Good Evening , use evening_greet tool to greet user.
    """,
    tools=[evening_greet,morning_greet],) 