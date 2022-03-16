import string
import nltk
from nltk.corpus import cess_esp #Corpus español
from nltk.corpus import stopwords

import BPE

corpus = [i.lower() for i in cess_esp.words()]

tokens = len(corpus)
tipos = len(set(corpus))
print('Número de tókens: ', tokens)
print('Número de tipos: ', tipos)

clean_corpus = [i for i in corpus if i.isalpha()]

#nltk.download('stopwords')
stopwords = set(stopwords.words('spanish'))
print()

clean_corpus = [i for i in clean_corpus if i not in stopwords]

print(clean_corpus[:200])

BPE.BPE(clean_corpus)