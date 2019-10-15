
import string

from app.helper_text import main_clean, clean

def test_clean():
    # it removes stopwords and punctuation, and lowercases the results:
    assert clean("Hello world! is a message from me and us") == "hello world message us"

def test_main_clean():
    # it converts text into a vector:
    results = main_clean("Hello world")
    #assert results[0] == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15857, 4284]]
    #assert results[1] == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15753, 4278]]
    assert results[0][0].tolist() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15857, 4284]
    assert results[1][0].tolist() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15753, 4278]

def test_remove_punctuation():
    assert "!" not in "Hello world!".translate(str.maketrans('', '', string.punctuation))
