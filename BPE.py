def BPE(corpus):
    tmp = corpus[:200]
    pair_list = []
    #Separar en pares.
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
    print([max_count, max_pair])

