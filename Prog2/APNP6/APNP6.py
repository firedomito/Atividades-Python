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

    for i in range(len(tmp_select)):
        timer.append(dicionario[lstMetodos[0]][i])
        timer.append(dicionario[lstMetodos[1]][i])
        timer.append(dicionario[lstMetodos[2]][i])

        plt.bar(lstMetodos, timer) 
        plt.ylabel("Tempo de Execucao") 
        plt.title("Tempo por Método") 
        plt.show()
        timer = []
    





if __name__ == "__main__":
    main()
