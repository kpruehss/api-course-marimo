# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.23.3",
#     "python-dotenv>=1.2.3",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    from dotenv import load_dotenv

    load_dotenv()
    return


if __name__ == "__main__":
    app.run()
