from . import predictions

def test_predictions():
    result = predictions.my_prediction()
    print(result)
    assert 'prediction' not in result