from keras.engine.training import Model

from app.model import unweighted_model, load_model

def test_unweighted_model():
    assert isinstance(unweighted_model(), Model)

def test_load_model():
    assert isinstance(load_model(), Model)
