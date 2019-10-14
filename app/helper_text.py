# for text processing and formatting the tweets

from wordsegment import load, segment
import re
import string
from nltk.corpus import stopwords # FYI: might need to also nltk.download()

from keras.preprocessing import sequence

from app.dictionaries import load_dictionaries

#from app.storage_service import BOT_ENV
#if BOT_ENV == "production":
#     nltk.download('stopwords')

load()

dictionary, dictionary_s = load_dictionaries()

def my_replace(match):
    match = match.group()
    return ' '.join(segment(match))

def process(twt):
    try:
        return(re.sub('#\w+', my_replace, twt))
    except Exception as e:
        return(None)

def clean(twt):
    #remove punctuation
    try:
        twt = twt.translate(str.maketrans('','',string.punctuation))
        twt = twt.split()
        twt = [i.lower() for i in twt]
        twt = [i for i in twt if 'htt' not in i and
                                      i not in stopwords.words('english')]
        twt = ' '.join(twt)
        return(twt)
    except Exception as e:
        print(e)
        return(None)

#transform takes a clean tweet and tokenize it
def transform(twt, seq_len):
    twt = clean(twt).split()
    l = []
    for i in twt:
        try:
            l.append(1 + dictionary.token2id[i])
        except:
            l.append(0)
    twt = sequence.pad_sequences([l], maxlen=seq_len)
    return(twt)

def transform_s(twt, seq_len):
    twt = clean(twt).split()
    l = []
    for i in twt:
        try:
            #print(i)
            l.append(1 + dictionary_s.token2id[i])
        except Exception as e:
            #print(e)
            l.append(0)
    twt = sequence.pad_sequences([l], maxlen=seq_len)
    return(twt)

def main_clean(twt):
    #segment
    twt_s = process(twt)
    #clean
    twt = clean(twt)
    twt_s = clean(twt_s)
    #transform
    twt = transform(twt, 20)
    twt_s = transform_s(twt_s, 20)
    #make x
    x = [twt, twt_s]
    return(x)


if __name__ == "__main__":
    english_stopwords = stopwords.words("english")

    print("ENGLISH STOPWORDS", len(english_stopwords), "...")

    for word in english_stopwords:
        print(" + ", word)
