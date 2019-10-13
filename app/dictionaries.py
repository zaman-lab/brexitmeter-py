
from os

from gensim.corpora import Dictionary

from app.storage import STORAGE_ENV

def load_dictionaries(storage_env=STORAGE_ENV):
	print(f"LOADING DICTIONARIES FROM {storage_env.upper()} STORAGE")
	if storage_env == "remote":
		dictionaries_dirpath =
	elif model_env == "local":
		dictionaries_dirpath = os.path.join(os.path.dirname(__file__), "..", "dictionary")

	dict1_filepath = os.path.join(dictionaries_dirpath, "dic.txt")
	dict2_filepath = os.path.join(dictionaries_dirpath, "dic_s.txt")

	dict1 = Dictionary.load(dict1_filepath)
	dict2 = Dictionary.load(dict2_filepath)
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

	#breakpoint()
