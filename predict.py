import joblib
import numpy as np
import flask

model = joblib.load("model.keras")

app = flask.Flask('app')

@app.route("/")
def index():
    return flask.render_template('predict.html')

@app.route("/predict")
def predict():
    args = flask.request.args
    r, g, b = int(args['r']), int(args['g']), int(args['b'])
    prediction = model.predict(np.array([[r/255, g/255, b/255]]))
    return flask.jsonify(prediction.tolist()[0])

app.run('0.0.0.0', port=8080)

np.array([]).tolist()