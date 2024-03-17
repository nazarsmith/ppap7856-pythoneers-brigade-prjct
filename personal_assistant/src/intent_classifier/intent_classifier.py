from keras.utils import pad_sequences
import numpy as np
import os
import pathlib
import pickle
import keras


class IntentClassifier:
    def __init__(self):
        res_pth = os.path.join(str(pathlib.Path(__file__).parents[2]), "resources")
        # Load tokenizer
        with open(os.path.join(res_pth, "tokenizer.pickle"), "rb") as handle:
            self.tokenizer = pickle.load(handle)
        # Load preprocessing parameters
        with open(os.path.join(res_pth, "preprocessing_params.pickle"), "rb") as handle:
            self.preprocessing_params = pickle.load(handle)

        self.model = keras.models.load_model(os.path.join(res_pth, "intent_cat_v3"))
        self.labels_dict = {
            0: "add-note",
            1: "add-note_tag",
            2: "delete-contact",
            3: "add-contact",
            4: "contact-remove_email",
            5: "add-contact_birthday",
            6: "show-all",
            7: "contact-remove_phone",
            8: "contact-change_email",
            9: "find-note",
            10: "find-contact",
            11: "contact-change_phone",
            12: "show-birthday",
        }

    def predict(self, sentence="i want to add a new contact"):

        self.PAD = self.preprocessing_params["PAD"]
        self.TRUNC = self.preprocessing_params["TRUNC"]
        self.MAX_LEN = self.preprocessing_params["MAX_LEN"]

        test_sentence = [sentence]

        test_sequence = self.tokenizer.texts_to_sequences(texts=test_sentence)

        test_sequence = pad_sequences(
            test_sequence, padding=self.PAD, truncating=self.TRUNC, maxlen=self.MAX_LEN
        )
        predicted = self.model.predict(test_sequence, verbose=0)
        probable_intent_key = np.where(predicted[0] == max(predicted[0]))[0][0]
        probable_intent = self.labels_dict[probable_intent_key]
        return probable_intent
