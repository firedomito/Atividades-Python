import random

def ord_select(lista):
    lstNum = len(lista)
    # Percorre o arranjo A.
    for i in range(lstNum):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, lstNum):
            if lista[minimo] > lista[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        lista[i], lista[minimo] = lista[minimo], lista[i]



def ord_insert(lista):
    lstNum = len(lista)
    # Percorre o arranjo A.
    for j in range(1, lstNum):
        chave = lista[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave


