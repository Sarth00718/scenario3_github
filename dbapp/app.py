from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "mydb.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Prediction(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    prediction = db.Column(db.String(50))


with app.app_context():
    db.create_all()


@app.route("/add_record", methods=["POST"])
def add_record():
    data = request.get_json()

    new_record = Prediction(
        sepal_length=data["sl"],
        sepal_width=data["sw"],
        petal_length=data["pl"],
        petal_width=data["pw"],
        prediction=data["prediction"]
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({
        "message": "Record added successfully"
    })


@app.route("/records", methods=["GET"])
def get_records():
    records = Prediction.query.all()

    result = []

    for record in records:
        result.append({
            "id": record.id,
            "sl": record.sepal_length,
            "sw": record.sepal_width,
            "pl": record.petal_length,
            "pw": record.petal_width,
            "prediction": record.prediction
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
