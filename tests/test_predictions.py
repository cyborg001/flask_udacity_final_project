from tests import predictions

def test_predictions():
    result = predictions.predictions()
    assert type(result) == type(dict())