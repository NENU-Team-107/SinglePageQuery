from flask import Flask

import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def Home():
    """
    This function will return a page contained things as follow:
        1. A select input (i.e. a list of tables in data)
        2. Two buttons, one is `Submit` to display a overview of table, the other is `Reset` to clear the select input
    """
    pass


@app.route("/details", method=["GET"])
def Tables():
    """
    This function will do things as followed:
        1. Get the table name from GET parameters
        2. Handler the file into dataframe according to the suffix of filename
        3. Render the dataframe (i.e. the overview of table) into HTML
        4. Render the query page as this:

        [this is a placeholder for items] [and/or] [button to increase or decrease the number of conditional statements]
    """
    pass


@app.route("/query", method=["POST"])
def Query():
    """
    This function will do things as followed:
        1. Get the query from POST parameters
        2. Execute the query
        3. Render the page with queryed data(and its query condition)
    """
    pass
