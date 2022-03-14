import string
import nltk
from nltk.corpus import cess_esp #Corpus español

corpus = [i.lower() for i in cess_esp.words()]

tokens = len(corpus)
tipos = len(set(corpus))
print('Número de tókens: ', tokens)
print('Número de tipos: ', tipos)

clean_corpus = [i for i in corpus if i.isalpha()]
print(clean_corpus[:200])
