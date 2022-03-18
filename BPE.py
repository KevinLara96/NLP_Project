import collections

from click import pass_obj

pair_list = collections.defaultdict(int)

def find_vocab(corpus):
    global pair_list
    
    vocab = collections.Counter(corpus)
    for i, freq in vocab.items():
        char = i.split()
        for j in range( len(char)-1 ):
            pair_list[char[j], char[j+1]] += freq
    
    max_ = 0
    letter = ()
    for pair, freq in pair_list.items():
        if(freq > max_):
            max_ = freq
            letter = pair
    print(letter, max_)

    for i in range(100):
        for j in range(0, len(corpus[i])-2, 2):
            if(letter[0]==corpus[i][j] and letter[1]==corpus[i][j+2]):
                print(letter[0], letter[1], ' -> ', corpus[i][j], corpus[i][j+2])
                corpus[i] = corpus[i][0:j+1:] + corpus[i][j+2::]
                print(corpus[i])
        print()
