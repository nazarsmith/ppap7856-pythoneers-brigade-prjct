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
        with open(os.path.join(res_pth, "tokenizer_v5.pickle"), "rb") as handle:
            self.tokenizer = pickle.load(handle)
        # Load preprocessing parameters
        with open(
            os.path.join(res_pth, "preprocessing_params_v5.pickle"), "rb"
        ) as handle:
            self.preprocessing_params = pickle.load(handle)

        self.model = keras.models.load_model(os.path.join(res_pth, "intent_cat_v5"))
        self.labels_dict = {
            0: "add-note",
            1: "edit-note",
            2: "add-birthday",
            3: "show-all-notes",
            4: "add-contact",
            5: "delete-note",
            6: "delete-contact",
            7: "delete-email",
            8: "change-phone",
            9: "find-contact",
            10: "show-all",
            11: "remove-phone",
            12: "find-note",
            13: "change-email",
            14: "birthdays",
            15: "add-email",
            16: "show-birthday",
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
