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
import numpy as np
from funcoes import *

def main():

    # DECLARAÇÃO DE VARIAVEIS #
    lstMetodos = ["Select", "Insert", "Sort"]
    tmp_select = []
    tmp_insert = []
    tmp_sort = []
    dicionario = {}

    #Gera lista de valores aleatorios com 10 unidades.
    lst10 = random.sample(range(-10000, 10000), 10)
    lst10_1 = lst10.copy()
    lst10_2 = lst10.copy()
    lst10_3 = lst10.copy()

    #Gera lista de valores aleatorios com 100 unidades.
    lst100 = random.sample(range(-10000, 10000 ), 100)
    lst100_1 = lst100.copy()
    lst100_2 = lst100.copy()
    lst100_3 = lst100.copy()

    #Gera lista de valores aleatorios com 1000 unidades.
    lst1000 = random.sample(range(-10000, 10000 ), 1000)
    lst1000_1 = lst1000.copy()
    lst1000_2 = lst1000.copy()
    lst1000_3 = lst1000.copy()

    #Gera lista de valores aleatorios com 10000 unidades.
    lst10000 = random.sample(range(-10000, 10000 ), 10000)
    lst10000_1 = lst10000.copy()
    lst10000_2 = lst10000.copy()
    lst10000_3 = lst10000.copy()

    #Gera lista de valores aleatorios com 100000 unidades.
    lst100000 = random.sample(range(-100000, 100000 ), 100000)
    lst100000_1 = lst10000.copy()
    lst100000_2 = lst100000.copy()
    lst100000_3 = lst100000.copy()

    #10 UNIDADES. Ordenação por Select
    agora = time.process_time()
    ord_select(lst10_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)
  
    #10 UNIDADES. Ordenação por Insert
    agora = time.process_time()
    ord_insert(lst10_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    #10 UNIDADES. Ordenação por Sort
    agora = time.process_time()
    lst10_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)


    #100 UNIDADES. Ordenação por Select
    agora = time.process_time()
    ord_select(lst100_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    #100 UNIDADES. Ordenação por Insert
    agora = time.process_time()
    ord_insert(lst100_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    #100 UNIDADES. Ordenação por Sort
    agora = time.process_time()
    lst100_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)


    #1000 UNIDADES. Ordenação por Select
    agora = time.process_time()
    ord_select(lst1000_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    #1000 UNIDADES. Ordenação por Insert
    agora = time.process_time()
    ord_insert(lst1000_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    #1000 UNIDADES. Ordenação por Sort
    agora = time.process_time()
    lst1000_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)

    #10.000 UNIDADES. Ordenação por Select
    agora = time.process_time()
    ord_select(lst10000_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    #10.000 UNIDADES. Ordenação por Insert
    agora = time.process_time()
    ord_insert(lst10000_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)
    
    #10.000 UNIDADES. Ordenação por Sort
    agora = time.process_time()
    lst10000_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)


    #100.000 UNIDADES. Ordenação por Select
    agora = time.process_time()
    ord_select(lst100000_1)
    tempo_decorrido = time.process_time() - agora
    tmp_select.append(tempo_decorrido)

    #100.000 UNIDADES. Ordenação por Insert
    agora = time.process_time()
    ord_insert(lst100000_2)
    tempo_decorrido = time.process_time() - agora
    tmp_insert.append(tempo_decorrido)

    #100.000 UNIDADES. Ordenação por Sort
    agora = time.process_time()
    lst100000_3.sort()
    tempo_decorrido = time.process_time() - agora
    tmp_sort.append(tempo_decorrido)

    # Adiciona o tempo gasto para execução e os metodos no dicionario. #
    dicionario[lstMetodos[0]] = tmp_select
    dicionario[lstMetodos[1]] = tmp_insert
    dicionario[lstMetodos[2]] = tmp_sort

    # SAIDA DE DADOS #
    print(dicionario)
    

    # DECLARAÇÃO DE VARIAVEL #
    timer = []

    
    # Gera o grafico com os valores de 100000 #
    timer.append(dicionario[lstMetodos[0]][4])
    timer.append(dicionario[lstMetodos[1]][4])
    timer.append(dicionario[lstMetodos[2]][4])
    plt.bar(lstMetodos, timer)
    plt.show()


    vazio = ' '
    lstNum = [10, 100, 1000, 10000, 100000]
    print('_' * 78)

    #Printa a variavel lstNum em ordem para formar a tabela
    print(f'|{vazio:>13}| {lstNum[0]:> 12} {lstNum[1]:> 13} {lstNum[2]:> 13} {lstNum[3]:> 13} {lstNum[4]:> 13}')

    #Print Tabela da Ordenação por Select Insert e Sort
    for key in dicionario:
        print(f'|{key:<13}| {dicionario[key][0]:>13,.5f} {dicionario[key][1]:>13,.5f} {dicionario[key][2]:>13,.5f} {dicionario[key][3]:>13,.5f} {dicionario[key][4]:>13,.5f}')
    print('_' * 78)



    # Inicio codigo BUSCA SEQUENCIAL E BINARIA #
    lstNaoOrd = random.sample(range(-100000, 100000 ), 100000)
    lstOrd = lstNaoOrd.copy()
    lstOrd.sort()

    
    inicioOrd = lstNaoOrd[0]
    meioOrd = lstNaoOrd[len(lstNaoOrd)//2]
    fimOrd = lstNaoOrd[len(lstNaoOrd)- 1]

    #Fora da Lista
    outList = 100001

    # DECLARAÇÃO DE VARIAVEIS #
    metodosBin = ['Busca Sequencial', 'Busca Binaria']
    tmp_sequencial = []
    tmp_binario = []
    dicBin = {}


    # Busca sequencial abaixo #
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

    #Adiciona o tempo gasto na busca sequencial ao dicionario.
    dicBin[metodosBin[0]] = tmp_sequencial


    # Busca Binaria abaixo #
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

    #Adiciona o tempo gasto na busca binaria ao dicionario.
    dicBin[metodosBin[1]] = tmp_binario


    # Print do dicionario da busca sequencial e binario
    print (dicBin)
    
    espacobranco = ' '
    sequencia = ['primeiro', 'ultimo', 'central', 'nao existente']

    print('_' * 81)

    #Printa a variavel Sequencia em ordem para formar a tabela
    print(f'|{espacobranco:>18}| {sequencia[0]:>13} {sequencia[1]:>12} {sequencia[2]:>14} {sequencia[3]:>18}|')
    
    #Print Tabela da Busca Sequencial e Binaria
    for key in dicBin:
        print(f'|{key:<18}| {dicBin[key][0]:>13,.5f} {dicBin[key][1]:>13,.5f} {dicBin[key][2]:>13,.5f} {dicBin[key][3]:>18,.5f}|')
    
    print('_' * 81)



    #Inicio do grafico dos tempos binarios e sequencial
    y1 = tmp_binario
    y2 = tmp_sequencial

    #Tamanho das Barras
    bwidth = 0.25

    x1 = np.arange(len(tmp_binario))
    x2 = [i + bwidth for i in x1]


    plt.bar(x1, y1, color='#4287f5', width=bwidth, label='Binario')
    plt.bar(x2, y2, color = '#19faa0', width = bwidth, label = 'Sequencial')

    # Gera o grafico de barras 
    plt.ylabel("Tempo Decorrido") # Nome dos elementos do Y
    plt.xlabel("Elementos") # Nome dos elementos do X
    plt.xticks([r + bwidth for r in range(len(y1))], ['primeiro', 'ultimo', 'central', 'nao existente']) # Distribui as legendas uniformemente
    plt.title("Tempo por Elemento") # Titulo da tabela

    plt.legend() # Cria legenda 
    plt.show() # Exibe o grafico




if __name__ == "__main__":
    main()
