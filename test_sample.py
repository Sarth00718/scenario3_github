"""
Basic smoke tests for the webapp's prediction logic.
Runs inside the cntwebapp container via: docker exec cntwebapp pytest test_sample.py -v

Inside the container:
  WORKDIR = /app
  model.pkl is at /app/model.pkl  (copied by Dockerfile)
"""

import joblib
import numpy as np


def test_model_loads():
    """Model file must be loadable."""
    model = joblib.load("model.pkl")
    assert model is not None


def test_model_predicts_valid_class():
    """Model must return one of the three Iris class names."""
    model = joblib.load("model.pkl")
    valid_classes = {"Iris-setosa", "Iris-versicolor", "Iris-virginica"}

    sample = np.array([[5.1, 3.5, 1.4, 0.2]])   # classic setosa sample
    prediction = str(model.predict(sample)[0])

    assert prediction in valid_classes, (
        f"Unexpected prediction: {prediction}"
    )


def test_model_batch_prediction():
    """Model should handle a batch of inputs without errors."""
    model = joblib.load("model.pkl")
    samples = np.array([
        [5.1, 3.5, 1.4, 0.2],   # setosa
        [6.7, 3.0, 5.2, 2.3],   # virginica
        [5.9, 3.0, 4.2, 1.5],   # versicolor
    ])
    predictions = model.predict(samples)
    assert len(predictions) == 3
