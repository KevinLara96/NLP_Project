vocab = set()

def find_vocab(corpus):
    global vocab

    string = ''
    for i in corpus:
        for j in i:
            string += j
    vocab = set(string)
    print(vocab)



def BPE(corpus, k):
    global vocab

    for count in range(k):
        tmp = corpus[:200]
        pair_list = []
        #Separar en pares de símbolos.
        for i in tmp:
            for j in range( len(i)-1 ):
                pair_list.append( i[j:j+2] )

        #Obtener la frecuencia de cada par.
        pair_counter = []
        for i in pair_list:
            pair_counter.append( [i,pair_list.count(i)] )

        #Obtener la frecuencia máxima.
        for i in pair_counter:
            max_count = 0
            max_pair = ''
            if(i[1] > max_count):
                max_count = i[1]
                max_pair = i[0]
        if [max_pair, max_count] in pair_counter:
            pair_counter.remove([max_pair, max_count])

        print([max_pair, max_count])
        vocab.add(max_pair)
        print(vocab)
        print('\n')