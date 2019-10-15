
import os
from gensim.corpora import Dictionary

from app.storage_service import STORAGE_ENV, dictionaries_dirpath

def load_dictionaries(storage_env="local"):
	dirpath = dictionaries_dirpath(storage_env)
	if storage_env == "local":
		dict1 = Dictionary.load(os.path.join(dirpath, "dic.txt"))
		dict2 = Dictionary.load(os.path.join(dirpath, "dic_s.txt"))
	elif storage_env == "remote":
		# todo: construct Dictionary objects from remote file contents
		# texts = [
		# 	['human', 'interface', 'computer']
		# ]
		# my_dict = Dictionary(texts)
		raise NotImplementedError

	return dict1, dict2

if __name__ == "__main__":

	texts = [
		['human', 'interface', 'computer']
	]
	my_dict = Dictionary(texts)
	for s in my_dict.iteritems():
		print(s)

	d1, d2 = load_dictionaries()

	print("-----------------------------")
	print("DICTIONARY 1", type(d1), len(d1))
	for s in d1.iteritems():
		print(s)

	print("-----------------------------")
	print("DICTIONARY 2", type(d1), len(d1))
	for s in d2.iteritems():
		print(s)
