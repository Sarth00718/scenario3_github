from flask import Flask, render_template, request
import requests
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

DB_SERVICE_URL = "http://dbapp:8000"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    sl = float(request.form["sepal_length"])
    sw = float(request.form["sepal_width"])
    pl = float(request.form["petal_length"])
    pw = float(request.form["petal_width"])

    result = model.predict([[
        sl,sw,pl,pw
    ]])

    prediction = str(result[0])

    data = {
        "sl": sl,
        "sw": sw,
        "pl": pl,
        "pw": pw,
        "prediction": prediction
    }

    response = requests.post( f"{DB_SERVICE_URL}/add_record",json=data )

    return render_template(
        "index.html",
        prediction=prediction
    )


@app.route("/show_records")
def show_records():
    response = requests.get( f"{DB_SERVICE_URL}/records" )

    records = response.json()

    return render_template(
        "records.html",
        records=records
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
