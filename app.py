from flask import Flask, render_template, request, send_from_directory
import dbfread
import pandas as pd
import os

app = Flask(__name__)

filename_list = []
data = pd.DataFrame()


@app.route("/", methods=["GET"])
def Home():
    """
    This function will return a page contained things as follow:
        1. A select input (i.e. a list of tables in data)
        2. Two buttons, one is `Submit` to display a overview of table, the other is `Reset` to clear the select input
    """
    global filename_list
    if filename_list == []:
        full_filename_list = os.listdir("data")
        filename_list = [
            f for f in full_filename_list if f.endswith(".dbf") or f.endswith(".xlsx") or f.endswith(".xls")
        ]
    return render_template("home.html", filename_list=filename_list)


@app.route("/details", methods=["POST"])
def Tables():
    """
    This function will do things as followed:
        1. Get the table name from GET parameters
        2. Handler the file into dataframe according to the suffix of filename
        3. Render the dataframe (i.e. the overview of table) into HTML
        4. Render the query page as this:

        [this is a placeholder for items] [and/or] [button to increase or decrease the number of conditional statements]
    """
    global data
    filename = request.form["filename"]
    if filename_list.count(filename) == 0:
        return NotFound()
    if filename.endswith(".dbf"):
        file = dbfread.DBF("data/" + filename)
        data = pd.DataFrame(iter(file))
    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        data = pd.read_excel("data/" + filename, sheet_name=0)
    else:
        return NotFound()

    return render_template("details.html", filename=filename, data=data.head(30))


@app.route("/query", methods=["POST"])
def Query():
    """
    This function will do things as followed:
        1. Get the query from POST parameters
        2. Execute the query
        3. Render the page with queryed data(and its query condition)
    """
    global data
    conditions = dict(request.form)
    conditions_list = []
    for i in range(0, (len(conditions) - 3) // 4):
        column = conditions[f"conditions[{i}][column]"]
        operator = conditions[f"conditions[{i}][operator]"]
        value = conditions[f"conditions[{i}][value]"]

        if operator == "是":
            conditions_expr = data[column] == value
        elif operator == "不是":
            conditions_expr = data[column] != value
        elif operator == "像":
            conditions_expr = data[column].str.contains(value)
        elif operator == ">":
            conditions_expr = data[column] > value
        elif operator == "<":
            conditions_expr = data[column] < value
        elif operator == ">=":
            conditions_expr = data[column] >= value
        elif operator == "<=":
            conditions_expr = data[column] <= value
        else:
            return NotFound()
        conditions_list.append(conditions_expr)
    combined_conditions = conditions_list[0]
    for i in range(1, len(conditions_list)):
        condition = conditions[f"conditions[{i}][condition]"]
        if condition == "并且":
            combined_conditions = combined_conditions & conditions_list[i]
        else:
            combined_conditions = combined_conditions | conditions_list[i]

    filtered_data = data[combined_conditions]
    return render_template("query.html", data=filtered_data)


@app.route("/favicon.ico")
def Favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico")

@app.errorhandler(404)
def NotFound():
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
