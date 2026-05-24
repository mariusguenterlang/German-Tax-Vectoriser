'''
This embedding approach follows the Bag of Words (BoW) model, which represents text data as a collection of word frequencies.
'''

import pandas as pd
import spacy

nlp = spacy.load("de_core_news_sm")

df = pd.read_csv("Downloads/Steuergesetze/extracted/estg.csv")