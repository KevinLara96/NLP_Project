import collections

pair_list = collections.defaultdict(int)

'''
    Realiza el algoritmo BPE.
    @param: corpus. Corpus en español.
    @param: k. Número de iteraciones.
'''
def BPE(corpus, k): 
    global pair_list
    
    #Si llegamos al número de iteraciones, se termina el algoritmo.
    if(k==0):
        return corpus

    #Contamos el número de veces que aparece cada palabra en el corpus.
    #es del tipo: {'c a d e n a' : Frecuencia}
    vocab = collections.Counter(corpus)
    for i, freq in vocab.items(): #i->Palabra. freq->Número apariciones.
        char = i.split() #Char es una lista que contiene las letras individuales.
        for j in range( len(char)-1 ):
            pair_list[char[j], char[j+1]] += freq   #Se cuenta el número de apariciones de
                                                    #los pares de letras
    

    max_ = 0
    letter = ()
    #Se obtiene el par que más se repite.
    for pair, freq in pair_list.items():
        if(freq > max_):
            max_ = freq
            letter = pair
    #print(letter, max_)

    #Se reemplaza el par, eliminando el espacio entre ambas letras.
    for i in range(100):
        for j in range(0, len(corpus[i])-2, 2):
            if(letter[0]==corpus[i][j] and letter[1]==corpus[i][j+2]):
                corpus[i] = corpus[i][0:j+1:] + corpus[i][j+2::]    #Se elimina el espacio, creando una
                                                                    #creando una nueva cadena.

    return BPE(corpus, k-1) #Se repite el proceso.
