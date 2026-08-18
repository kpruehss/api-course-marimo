# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


app._unparsable_cell(
    r"""
    uv add anthropic
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
