# Mirascope 🤝 Nolita

This is a simple conversational chatbot that uses Nolita as a web browsing tool. It's on the model to determine when it needs to search the web. It's also a nice demo of how to build a custom tool in Mirascope.

### Getting Started

You have to be running Nolita locally to use this. You can find the repo [here](https://github.com/nolita-ai/nolita). Follow their installation instructions. To run the server, use the following command:

```
npx nolita serve
```

Once you have Nolita running, you can run the chatbot by activating the virtual environment and running the main script:

```
poetry install
poetry shell
python main.py
```