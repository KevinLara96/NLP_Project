#Aguilar Torres Karla Daniela
#Lara Sala Kevin Arturo
#Martınez Martınez Vanessa

#Práctica 2 - Se tuvieron algunos problemas con el entrenamiento de red, y los resultados no fueron los esperados

import numpy as np
import tqdm

def Red(sentences, clean_corpus):
    
    # Creación de bigramas a partir de nuestras oraciones
    test_list = [sentences] 
    
    res = [(x, i.split()[j + 1]) for i in test_list  
        for j, x in enumerate(i.split()) if j < len(i.split()) - 1] 
    
    print ("Pares a partir de contexto: " + str(res))
    bigramas = str(res)


    #Entrenamiento de red con los bigramas
    np.random.seed(0)
    #Parámetros determinados para el entrenamiento del modelo
    it_model = 50
    eta = 0.1
    N = len(clean_corpus)
    print(N)
    lineal = 180 #capa lineal
    tanh = 300 #capa con tanh

    # Preparación del modelo neuronal
    #Para la capa de embeding
    C = np.random.randn(lineal,N) / np.sqrt(N)
    #Para la capa hiperbolica
    W = np.random.randn(tanh,lineal) / np.sqrt(tanh)
    b = np.ones(tanh)
    #Para la capa de salida
    U = np.random.randn(N,tanh) / np.sqrt(tanh)
    c = np.ones(N)


    for i in tqdm(range(0,it_model)):    
        for bg in bigramas:
        # Arquitectura Forward       
            #Capa de embbeding
            embeddingLayer = C.T[bg[0]]
            #Capa oculta 
            hiddenLayer= np.tanh(np.dot(W,embeddingLayer) + b)
            pre_hiddenLayer = np.dot(U,hiddenLayer) + c
            outLayer = np.exp(pre_hiddenLayer - np.max(pre_hiddenLayer))
            f = outLayer/outLayer.sum(0)
            
        #Backpropagation
        #Las variables de backpropagation
            #Capa de salida
            d_out = f
            d_out[bg[1]] -= 1
            #Capa oculta
            d_h = (1-hiddenLayer**2)*np.dot(U.T,d_out) 
            #Capa embedding
            d_c = np.dot(W.T,d_h)
            c -= eta*d_out
        
    #Gradiente descendiente 
    #Actualizaciones de los pesos a partir de las variables
        #Capa de salida
        U -= eta*np.outer(d_out,hiddenLayer)
        #Capa oculta
        W -= eta*np.outer(d_h,embeddingLayer)
        b -=eta*d_h
        #Capa de embedding
        C.T[bg[0]] -= eta*d_c
        #Capa de embbeding
        embeddingLayer = C.T[x]
        #Cpa oculta y pre activación
        hiddenLayer= np.tanh(np.dot(W,embeddingLayer) + b)
        pre_hiddenLayer = np.dot(U,hiddenLayer) + c
        #Salida - se resta el max para evitar errores
        outLayer = np.exp(pre_hiddenLayer - np.max(pre_hiddenLayer))
        #Softmax
        f = outLayer/outLayer.sum(0)

    #Evaluación del modelo
    H = 0.0
    for cad in clean_corpus:
        #Longitud de la cadena
        M = len(cad)
        #Obtenemos la entropía cruzada de la cadena
        if cad == 0:
            pass
        else:
            H -= (1./M)*(np.log(cad)/np.log(2))
            

    print('Entropía promedio: {}\nPerplejidad total: {}'.format(H,2**H))

    #Los vectores de la capa de embedding se encuentran en 'C'
    dic_embedding = {}
    for element in C:
        for w in element:
            for i in range(0,len(element)):
                dic_embedding[i] = w
    #print(dic_embedding)