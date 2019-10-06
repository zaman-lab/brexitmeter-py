
from os import path

from gensim.corpora import Dictionary

def load_dictionaries():
	DICT1_FILEPATH = path.join(path.dirname(__file__), "..", "dictionary", "dic.txt")
	DICT2_FILEPATH = path.join(path.dirname(__file__), "..", "dictionary", "dic_s.txt")
    # what are the differences between these two dictionaries?
    # ... one helps for segmentation?
	dict1 = Dictionary.load(DICT1_FILEPATH)
	dict2 = Dictionary.load(DICT2_FILEPATH)
	return dict1, dict2

if __name__ == "__main__":

	d1, d2 = load_dictionaries()

	print("-----------------------------")
	print("DICTIONARY 1", type(d1), len(d1))
	for s in d1.iteritems():
		print(s)

	print("-----------------------------")
	print("DICTIONARY 2", type(d1), len(d1))
	for s in d2.iteritems():
		print(s)

	breakpoint()
