import string
import nltk
from nltk.corpus import cess_esp #Corpus español
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('cess_esp')

import BPE #Se importa el módulo del algoritmo.

#Pasamos el corpus a minúsculas.
corpus = [i.lower() for i in cess_esp.words()]

tokens = len(corpus)
tipos = len(set(corpus))
print('Número de tókens: ', tokens)
print('Número de tipos: ', tipos)


#Se eliminan caracteres y cadenas que no sean puramente letras.
#e.g. signos de exclamación, interrogación, etc.
clean_corpus = [i for i in corpus if i.isalpha()]

#Se eliminan las stopwords en español del corpus.
stopwords = set(stopwords.words('spanish'))
clean_corpus = [i for i in clean_corpus if i not in stopwords]


#Se separan las palabras en caracteres separados por espacios.
clean_corpus = [' '.join(list(x)) for x in clean_corpus]


clean_corpus = BPE.BPE(clean_corpus[:100], 20)
for i in range(len(clean_corpus)):
    print(clean_corpus[i])
#Descomentar para imprimir el corpus actualizado.
#print(clean_corpus)