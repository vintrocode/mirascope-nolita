import os
from dotenv import load_dotenv
from calls import Chatbot

def main():
    load_dotenv()
    history = []
    chatbot = Chatbot(context="None", history=history, user_input="")

    print("Welcome to the Web-Browsing Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'exit':
            break

        chatbot.user_input = user_input
        chatbot.history = history

        response = chatbot.call()
        assistant_response = response.content

        print(response)

        # Check if the response contains a tool use
        if response.choices[0].finish_reason == 'tool_calls':
            print("\nAssistant is browsing the web...")
            tool = response.tool
            # Override the max_iterations argument
            tool_args = tool.args.copy()
            tool_args['max_iterations'] = 5  # You can set this to any desired value
            tool_args['start_url'] = "https://www.google.com"
            print(f"\nTool: {tool}")
            web_content = tool.fn(**tool_args)
            print(f"\nWeb Content: {web_content}")
            chatbot.context = web_content['description']
            follow_up = chatbot.call()
            print(f"\nFollow-up: {follow_up.content}")
            assistant_response += follow_up.content

        print(f"\nAssistant: {assistant_response}")

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()
