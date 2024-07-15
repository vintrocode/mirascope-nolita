from typing import List
from mirascope.openai import OpenAICall, OpenAICallParams
from tools import NolitaBrowser


class Chatbot(OpenAICall):
    prompt_template = """
    SYSTEM: You are a helpful assistant with the ability to browse the web. Use the NolitaBrowser tool when you need to fetch information from the internet. If context exists, it will be provided to you here: {context}

    MESSAGES: {history}
    USER: {user_input}
    """
    context: str
    history: List[dict]
    user_input: str
    call_params = OpenAICallParams(model="gpt-4-turbo", tools=[NolitaBrowser])
