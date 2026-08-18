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

    return


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
    # Make a request
    import token
    message = client.messages.create(
      model=model,
      max_tokens=1000,
      messages=[
        {
          "role": "user",
          "content": "What is quantum computing? Answer in 1 sentence"
        }
      ]
    )
    return (message,)


@app.cell
def _(message):
    message
    return


if __name__ == "__main__":
    app.run()
