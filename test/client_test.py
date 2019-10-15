

from app.model import load_model
from app.client import classify

def test_classify():

    model = load_model()

    r1 = classify("I want the UK to stay EU #remain #remain #remain", model)
    assert round(float(r1["pro_brexit"]), 4) == 0.4284

    r2 = classify("I want the UK to leave EU #BrexitNow", model)
    assert round(float(r2["pro_brexit"]), 4) == 0.8875
