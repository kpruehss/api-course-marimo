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
    from anthropic.types import MessageParam

    def anthropic_model(messages, config):
        # mo.ui.chat hands us the full conversation history on every turn as a
        # list of ChatMessage objects (role/content) - no manual bookkeeping
        # (add_user_message/add_assistant_message) needed like in 001_requests.py.
        # Annotating as list[MessageParam] (rather than leaving it as a plain
        # dict) is what lets the type checker match these literals against the
        # SDK's TypedDict - a bare dict isn't considered TypedDict-compatible.
        # Filtering out "system" also matters here: MessageParam only allows
        # "user"/"assistant" roles, even though ChatMessage.role admits "system".
        api_messages: list[MessageParam] = [
            {"role": m.role, "content": m.content}
            for m in messages
            if m.role != "system"
        ]

        response = client.messages.create(
            model=model,
            max_tokens=1000,
            messages=api_messages,
        )

        return next(block.text for block in response.content if block.type == "text")

    return (anthropic_model,)


@app.cell
def _(anthropic_model, mo):
    chat = mo.ui.chat(anthropic_model)
    chat
    return (chat,)


@app.cell
def _(chat):
    # Reactive access to the transcript from any other cell - updates
    # automatically as the conversation progresses in the chat UI above.
    chat.value
    return


if __name__ == "__main__":
    app.run()
