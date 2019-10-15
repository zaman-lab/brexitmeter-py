
import os
import tensorflow as tf

from app.storage_service import weights_filepath, dictionaries_dirpath

def test_local_storage():
    local_filepaths = [
		weights_filepath("local"),
		os.path.join(dictionaries_dirpath("local"), "dic.txt"),
		os.path.join(dictionaries_dirpath("local"), "dic_s.txt"),
	]
    for filepath in local_filepaths:
        assert os.path.isfile(filepath)

def test_remote_storage():
    remote_filepaths = [
		weights_filepath("remote"),
		os.path.join(dictionaries_dirpath("remote"), "dic.txt"),
		os.path.join(dictionaries_dirpath("remote"), "dic_s.txt"),
	]
    for filepath in remote_filepaths:
        assert tf.io.gfile.exists(filepath)
