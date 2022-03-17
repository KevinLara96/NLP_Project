import string
import nltk
from nltk.corpus import cess_esp #Corpus español
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download('cess_esp')

import BPE

corpus = [i.lower() for i in cess_esp.words()]

tokens = len(corpus)
tipos = len(set(corpus))
print('Número de tókens: ', tokens)
print('Número de tipos: ', tipos)

clean_corpus = [i for i in corpus if i.isalpha()]

stopwords = set(stopwords.words('spanish'))
print()

clean_corpus = [i for i in clean_corpus if i not in stopwords]
clean_corpus = [' '.join(list(x)) for x in clean_corpus]


BPE.find_vocab(clean_corpus[:100])
#BPE.BPE(clean_corpus, 5)