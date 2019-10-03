#!/usr/bin/env python
# coding: utf-8

# #upload libraries
import numpy as np
import json
from os import listdir
from os.path import isfile, join
from itertools import islice
import re
import os.path


# In[1]:
from helper_text import main_clean




def compute_polarity(twt,model):
	print(twt)
	x, x_s = main_clean(twt)
	pro_pol = model.predict([x, x_s])[:,1]
	print('This tweet is ', pro_pol,' Pro Brexit')
	return pro_pol
