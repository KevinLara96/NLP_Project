import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from operator import itemgetter
from nltk.corpus import cess_esp
from collections import Counter
from nltk.corpus import brown


#Descarga del corpus
nltk.download('cess_esp')

#Obtener los tokens
#words = list(cess_esp.words())
words = list(brown.words())

#Pasar a minúsculas
words = [w.lower() for w in words]
words = [i for i in words if i.isalpha()]


#Obtener las frecuencias
word_freqs = Counter(words)

#Ordenas las frecuencias de mayor a menor
word_freqs = sorted(word_freqs.items(), key=itemgetter(1), reverse=True)

freqs = np.array([pair[1] for pair in word_freqs])

#Número de tipos N
N = len(freqs)
#Obtener los rangos
ranks = np.array(range(1,N+1))

#Obtenemos los logaritmos
log_freqs = np.log(freqs)
log_ranks = np.log(ranks)



#Plotep
plt.scatter(log_ranks, log_freqs)
plt.xlabel('log rangos')
plt.ylabel('log frecuencias')
plt.title('Corpus CESS (Zipf)')
#plt.show()

#Rangos
ranks_data = pd.DataFrame(data=log_ranks, columns=['log rangos'])
#Frecuencias
freqs_data = pd.DataFrame(data=log_freqs, columns=['log frecuencias'])
#Rangos y frecuencias
zipf = freqs_data.join(ranks_data)



#Estimación de parámetro
std_coeff = float(ranks_data.std())/float(ranks_data.std())
a = float(zipf.corr()['log rangos']['log frecuencias'])*std_coeff

print(a)

#Ploteo
plt.scatter(log_ranks, log_freqs, s=1, label='Datos originales')
plt.plot(log_ranks, a*log_ranks+log_freqs[0], c='r', label='Aproximación')
plt.xlabel('log rangos')
plt.ylabel('log frcuencias')
plt.title('Aproximación a curva Zipf')
plt.legend(bbox_to_anchor=(1, 1))
#plt.show()

#Función de probabilidad
f = ranks**a
probs = f/f.sum(0)

print(probs.sum(0))

#Muestreo de palabras por sus probabilidades
gen_words = np.random.choice([pair[0] for pair in word_freqs], size=100, p=probs)

text = ' '.join(gen_words)
print(text)
