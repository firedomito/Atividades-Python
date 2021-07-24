import random

# Função de ordenação por Select. Recebe uma Lista Numerica #
def ord_select(lista):
    lstNum = len(lista)
    # Percorre a lstNum
    for i in range(lstNum):
        # Encontra o elemento mínimo
        minimo = i
        for j in range(i + 1, lstNum):
            if lista[minimo] > lista[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        lista[i], lista[minimo] = lista[minimo], lista[i]


# Função de ordenação por Insert. Recebe uma Lista Numerica #
def ord_insert(lista):
    lstNum = len(lista)
    # Percorre a lstNum .
    for j in range(1, lstNum):
        chave = lista[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave


# Função de Busca Binaria. Recebe uma lista e um item que será procurado na lista. Retorna a posição do item #
def buscaBinaria(lista, item):
    esquerda = 0
    pos = -1
    fim = len(lista) - 1
    while esquerda <= fim and pos == -1:
        meio = (esquerda + fim) // 2
        if item == lista[meio]:
            pos = meio
        elif item < lista[meio]:
            fim = meio - 1
        else:
            esquerda = meio + 1
    return pos


# Função de Busca Sequencial. Recebe uma lista e um item que será procurado na lista. Retorna a posição do item #
def buscaSequencial(lista, item):
    pos = -1
    i = 0
    while i < len(lista) and pos == -1:
        if lista[i] == item:
            pos = i
        i += 1
    return pos

