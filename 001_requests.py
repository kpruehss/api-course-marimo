# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.122.0",
#     "marimo>=0.23.3",
#     "python-dotenv>=1.2.3",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import dotenv
    import anthropic
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from dotenv import load_dotenv

    load_dotenv()
    return


@app.cell
def _():
    # Setup the client
    from anthropic import Anthropic

    client = Anthropic()
    model = "claude-sonnet-5"
    return client, model


@app.cell
def _(client, model):
    def add_user_message(messages, text):
      user_message = {"role": "user", "content": text}
      messages.append(user_message)

    def add_assistant_message(messages, text):
      assistant_message = {"role": "assistant", "content": text}
      messages.append(assistant_message)

    def chat(messages):
      message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
      )
      return message.content[0].text

    return add_assistant_message, add_user_message, chat


@app.cell
def _(add_assistant_message, add_user_message, chat, mo):
    messages = []

    add_user_message(messages, "Define quantum computing in one sentence")

    answer = chat(messages)

    # Take the answer and add it as an assistant message to preserve context
    add_assistant_message(messages, answer)

    # Add a followup question to the conversation
    add_user_message(messages, "Can you explain how quantum entanglement works in simple terms?")

    answer = chat(messages)
    mo.md(answer)
    return


if __name__ == "__main__":
    app.run()
