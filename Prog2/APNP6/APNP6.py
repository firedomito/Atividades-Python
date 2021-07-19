#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# APNP3.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################

import time
import random
from funcoes import *

def main():
    lstMetodos = ["Select", "Insert", "Sort"]
    tmp_select = []
    tmp_insert = []
    tmp_sort = []


    lst10_1 = random.sample(range(-10000, 10000), 10)
    lst10_2 = random.sample(range(-10000, 10000), 10)
    lst10_3 = random.sample(range(-10000, 10000), 10)


    lst100 = random.sample(range(-10000, 10000 ), 100)
    lst1000 = random.sample(range(-10000, 10000 ), 1000)
    lst10000 = random.sample(range(-10000, 10000 ), 10000)
    lst100000 = random.sample(range(-10000, 10000 ), 100000)




    agora = time.process_time()
    ord_select(lst10_1)
    tempo_decorrido = time.process_time() - agora
    print (tempo_decorrido)
    tmp_select.append(tempo_decorrido)
    
    

    agora = time.process_time()
    ord_insert(lst10_2)
    tempo_decorrido = time.process_time() - agora
    print (tempo_decorrido)
    tmp_insert.append(tempo_decorrido)


    agora = time.process_time()
    lst10_3.sort()
    tempo_decorrido = time.process_time() - agora
    print (tempo_decorrido)
    tmp_sort.append(tempo_decorrido)




    # print (lst10_1)
    # ord_select(lst10_1)
    # print (lst10_1)

    # print (lst10_2)
    # ord_insert(lst10_2)
    # print (lst10_2)
    
    # print (lst10_3)
    # lst10_3.sort()
    # print (lst10_3)






if __name__ == "__main__":
    main()
