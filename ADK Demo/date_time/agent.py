from google.adk.agents import Agent
from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    }    

root_agent = Agent(
    name = "tool_agent",
    model = "gemini-2.0-flash",
    description="An example agent that will provide the current date and time.",   
    instruction="""
    You are an AI Assistant that provides the current date and time when asked.
    """,  
    tools=[get_current_time]
)