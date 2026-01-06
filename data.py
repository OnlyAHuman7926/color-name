import flask, os
import numpy as np
import pandas as pd

flags = ['Black', 'Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Purple', 'White', 'Gray', 'Pink', 'Brown']

if os.path.exists('data.csv'):
    data = pd.read_csv("data.csv", sep=',')
else:
    thing = {
        'Red': [],
        'Green': [],
        'Blue': []
    }
    for i in range(len(flags)):
        thing[str(i)] = []
    data = pd.DataFrame(thing)
app = flask.Flask("app")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/add-data")
def add():
    global data
    args = flask.request.args
    r, g, b, flag = int(args['r']), int(args['g']), int(args['b']), int(args['flag'])
    other = {
        'Red': [r/255],
        'Green': [g/255],
        'Blue': [b/255]
    }
    for i in range(len(flags)):
        other[str(i)] = [int(i == flag)]
    data = pd.concat([data, pd.DataFrame(other)])
    print(data)
    return "asdf"

@app.route("/update-csv")
def update():
    data.to_csv("data.csv", sep=',')
    return "Updated data successfully!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)