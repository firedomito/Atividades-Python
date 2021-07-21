#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# APNP6.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################

import time
import random
from matplotlib import pyplot as plt
from numpy.lib.function_base import select
from funcoes import *

def main():

    lstMetodos = ["Select", "Insert", "Sort"]
    tmp_select = []
    tmp_insert = []
    tmp_sort = []
    dicionario = {}

    lst10 = random.sample(range(-10000, 10000), 10)
    lst10_1 = lst10.copy()
    lst10_2 = lst10.copy()
    lst10_3 = lst10.copy()


    lst100 = random.sample(range(-10000, 10000 ), 100)
    lst100_1 = lst100.copy()
    lst100_2 = lst100.copy()
    lst100_3 = lst100.copy()


    lst1000 = random.sample(range(-10000, 10000 ), 1000)
    lst1000_1 = lst1000.copy()
    lst1000_2 = lst1000.copy()
    lst1000_3 = lst1000.copy()


    lst10000 = random.sample(range(-10000, 10000 ), 10000)
    lst10000_1 = lst10000.copy()
    lst10000_2 = lst10000.copy()
    lst10000_3 = lst10000.copy()


    #lst100000 = random.sample(range(-10000, 10000 ), 100000)


    agora = time.process_time()
    ord_select(lst10_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)
  

    agora = time.process_time()
    ord_insert(lst10_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)


    agora = time.process_time()
    lst10_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)

    agora = time.process_time()
    ord_select(lst100_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    agora = time.process_time()
    ord_insert(lst100_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    agora = time.process_time()
    lst100_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)

    agora = time.process_time()
    ord_select(lst1000_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    agora = time.process_time()
    ord_insert(lst1000_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    
    agora = time.process_time()
    lst1000_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)



    agora = time.process_time()
    ord_select(lst10000_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    agora = time.process_time()
    ord_insert(lst10000_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    agora = time.process_time()
    lst10000_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)


    dicionario[lstMetodos[0]] = tmp_select
    dicionario[lstMetodos[1]] = tmp_insert
    dicionario[lstMetodos[2]] = tmp_sort

    print(dicionario)
    

    timer = []

    
    #Gera o grafico com os valores de 100000
    timer.append(dicionario[lstMetodos[0]][3])
    timer.append(dicionario[lstMetodos[1]][3])
    timer.append(dicionario[lstMetodos[2]][3])
    plt.bar(lstMetodos, timer)
    plt.show()

    vazio = ' '
    lstNum = [10, 100, 1000, 10000, 100000]
    print('_' * 78)
    print(f'|{vazio:>13}| {lstNum[0]:> 12} {lstNum[1]:> 13} {lstNum[2]:> 13} {lstNum[3]:> 13}')

    for key in dicionario:
        print(f'|{key:<13}| {dicionario[key][0]:>13,.5f} {dicionario[key][1]:>13,.5f} {dicionario[key][2]:>13,.5f} {dicionario[key][3]:>13,.5f}')
    print('_' * 78)



    # SEQUENCIA #
    lstNaoOrd = random.sample(range(-100000, 100000 ), 100000)
    lstOrd = lstNaoOrd.copy()
    lstOrd.sort()



    
    inicioOrd = lstNaoOrd[0]
    meioOrd = lstNaoOrd[len(lstNaoOrd)//2]
    fimOrd = lstNaoOrd[len(lstNaoOrd)- 1]

    #Fora da Lista
    outList = 100001

    metodosBin = ['Busca Sequencial', 'Busca Binaria']
    tmp_sequencial = []
    tmp_binario = []

    dicBin = {}

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, inicioOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_sequencial.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, fimOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_sequencial.append(tempo_decorrido)
    
    agora = time.process_time()
    buscaSequencial(lstNaoOrd, meioOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_sequencial.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, outList)
    tempo_decorrido = time.process_time() - agora
    tmp_sequencial.append(tempo_decorrido)


    dicBin[metodosBin[0]] = tmp_sequencial

    #Busca Binaria abaixo

    agora = time.process_time()
    buscaBinaria(lstOrd, inicioOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_binario.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstOrd, fimOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_binario.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstOrd, meioOrd)
    tempo_decorrido = time.process_time() - agora
    tmp_binario.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstOrd, outList)
    tempo_decorrido = time.process_time() - agora
    tmp_binario.append(tempo_decorrido)

    dicBin[metodosBin[1]] = tmp_binario


    print (dicBin)
    
    espacobranco = ' '
    sequencia = ['primeiro', 'ultimo', 'central', 'nao existente']

    print('_' * 81)
    print(f'|{espacobranco:>18}| {sequencia[0]:>13} {sequencia[1]:>12} {sequencia[2]:>14} {sequencia[3]:>18}|')
    
    for key in dicBin:
        print(f'|{key:<18}| {dicBin[key][0]:>13,.5f} {dicBin[key][1]:>13,.5f} {dicBin[key][2]:>13,.5f} {dicBin[key][3]:>18,.5f}|')
    
    print('_' * 81)

    


if __name__ == "__main__":
    main()
