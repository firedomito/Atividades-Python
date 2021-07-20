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



# def pesquisa_binaria(lista, item):
#     """Implementa pesquisa binária iterativamente."""
#     esquerda, direita = 0, len(A) - 1
#     while esquerda <= direita:
#         meio = (esquerda + direita) // 2
#         if A[meio] == item:
#             return meio
#         elif A[meio] > item:
#             direita = meio - 1
#         else: # A[meio] < item
#             esquerda = meio + 1
#     return -1

# def buscaSequencial(lista, elemento):
#     pos = int(0)
#     i = int(0)

#     pos = -1
#     i = 0
#     while i < len(lista) and pos == -1:
#         if lista[i] == elemento:
#             pos = i
#         i += 1
#     return pos

