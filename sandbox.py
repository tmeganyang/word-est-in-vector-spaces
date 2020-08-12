import json
import nltk
import numpy as np 
import matplotlib.pyplot as plt
import re

def download_punkt():
    nltk.download('punkt')

def get_parsed_document(raw_document):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    return sent_detector.tokenize(raw_document_data.strip().replace("\n", " ").lower())

def get_raw_document_data(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def get_word_vector(word, dictionary, document):
    word_dictionary = dict(english_dictionary)
    for sentence in parsed_document:
        if word in sentence:
            words = sentence.split(" ")
            for token in words:
                token = re.sub(r'[^a-zA-Z]', "", token)
                if token and token in english_dictionary.keys():
                    word_dictionary[token] = word_dictionary[token] + 1
        else:
            continue

    word_vector = np.array([])
    for value in word_dictionary.values():
        word_vector = np.append(word_vector, np.array(value))
    return word_vector

def find_match(vector, dictionary):
    # vector -> dictionary mapping
    

raw_document_data = get_raw_document_data('grimm.txt')[2692:]
raw_dictionary_data = get_raw_document_data('words_dictionary.json')

english_dictionary = json.loads(raw_dictionary_data)
parsed_document = get_parsed_document(raw_document_data)

word_1 = 'man'
word_2 = 'woman'
word_3 = 'king'
#v_1 - v_2 = v_3 - v_4
#v_4 = v_3 - v_1 + v_2
v_1 = get_word_vector(word_1, english_dictionary, parsed_document)
v_2 = get_word_vector(word_2, english_dictionary, parsed_document)
v_3 = get_word_vector(word_3, english_dictionary, parsed_document)
v_4 = v_3 - v_1 + v_2
print(v_1, v_2, v_3)




