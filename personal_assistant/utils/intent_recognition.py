from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
import keras
import tensorflow as tf
import numpy as np


import os
from personal_assistant import resources
import pathlib

import pickle

pth = os.path.join(str(pathlib.Path(__file__).parents[1]), "resources")
print(pth)

# Load tokenizer
with open(os.path.join(pth, "tokenizer.pickle"), "rb") as handle:
    tokenizer = pickle.load(handle)

# Load preprocessing parameters
with open(os.path.join(pth, "preprocessing_params.pickle"), "rb") as handle:
    preprocessing_params = pickle.load(handle)

PAD = preprocessing_params["PAD"]
TRUNC = preprocessing_params["TRUNC"]
MAX_LEN = preprocessing_params["MAX_LEN"]

print(PAD, TRUNC, MAX_LEN)

# model = tf.saved_model.load(os.path.join(pth, "intent_categorization.h5"))
# print(model)

test_sentence = ["i want to add a contact"]

test_sequence = tokenizer.texts_to_sequences(texts=test_sentence)
print(test_sequence)
test_sequence = pad_sequences(
    test_sequence, padding=PAD, truncating=TRUNC, maxlen=MAX_LEN
)
print(test_sequence, test_sequence.shape)
labels_dict = {
    "add-note": 0,
    "add-note_tag": 1,
    "delete-contact": 2,
    "add-contact": 3,
    "contact-remove_email": 4,
    "add-contact_birthday": 5,
    "show-all": 6,
    "contact-remove_phone": 7,
    "contact-change_email": 8,
    "find-note": 9,
    "find-contact": 10,
    "contact-change_phone": 11,
    "show-birthday": 12,
}
# print(dir(model))
# predicted = model(shape = test_sequence.shape, dtype=tf.float32, name='inputs')
# print(predicted)

model = keras.models.load_model(os.path.join(pth, "intent_cat_v3"))
# model = tf.saved_model.load(os.path.join(pth, "intent_cat_v2"))
print(model.summary())
predicted = model.predict(test_sequence)

print(predicted)
print(max(predicted[0]))
print(np.where(predicted[0] == max(predicted[0]))[0][0])

print(labels_dict)
