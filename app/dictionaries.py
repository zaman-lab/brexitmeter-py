
from os import path

from gensim.corpora import Dictionary

def load_dictionaries():
	DICT1_FILEPATH = path.join(path.dirname(__file__), "..", "dictionary", "dic.txt")
	DICT2_FILEPATH = path.join(path.dirname(__file__), "..", "dictionary", "dic_s.txt")
	dict1 = Dictionary.load(DICT1_FILEPATH)
	dict2 = Dictionary.load(DICT2_FILEPATH)
    # what are the differences between these two dictionaries?
    # ... oh, one helps for segmentation?
    # what are the datatypes?
	return dict1, dict2
