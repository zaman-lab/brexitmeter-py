
from gensim.corpora import Dictionary

from app.dictionaries import load_dictionaries

def test_load_dictionaries():

    d1, d2 = load_dictionaries()

    assert isinstance(d1, Dictionary)
    assert isinstance(d2, Dictionary)

    assert len(d1) == 224011
    assert len(d2) == 219691

    assert "remain" in d1.values()
    assert d1[124] == "remain"
    assert d1.id2token[124] == "remain"
    assert d1.token2id["remain"] == 124
