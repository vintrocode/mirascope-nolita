import requests
import os
from mirascope.base import tool_fn
from mirascope.openai import OpenAITool
from pydantic import Field

def browse_web(objective: str, start_url: str = "https://google.com", max_iterations: int = 3) -> str:

    browser_session = requests.post(
        "http://localhost:3000/browser/session/launch", 
        json={
            "headless": False,
            "agent": {
                "provider":"openai", 
                "model":"gpt-4", 
                "apiKey": os.getenv("OPENAI_API_KEY")
            },
        }
    )
    browser_session_id = browser_session.json()["sessionId"]

    page_id = requests.get(f"http://localhost:3000/{browser_session_id}/page/newPage").json()["pageId"]
    response = requests.post(f"http://localhost:3000/{browser_session_id}/page/{page_id}/goto", json={"url": start_url})
    response = requests.post(f"http://localhost:3000/{browser_session_id}/page/{page_id}/browse", json={"command": objective})
    requests.get(f"http://localhost:3000/browser/{browser_session_id}/close")

    return response.json()

    

@tool_fn(browse_web)
class NolitaBrowser(OpenAITool):
    """Run the Nolita Browser"""
    objective: str = Field(..., description="The objective of the web browsing.")
    start_url: str = Field(..., description="The URL of the web page to start browsing from.")
    max_iterations: int = Field(..., description="The maximum number of iterations to browse the web.")

