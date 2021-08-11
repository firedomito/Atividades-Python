#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# main.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################


from funcao import *
import json

def main():
    #declaração de variaveis
    nomeEntrada = input()


    # lê os dados do arquivo
    with open('entrada.txt', "rt") as nomeEntrada:
        #faz a leitura e o processamento das informações, retornando um dicionario 
        dic = leituraArq(nomeEntrada)

    # escreve o dicionario "dic" em um arquivo json, com indentação 4
    with open('dados.json', 'w') as dados:
        json.dump(dic, dados, indent=4)
    
    # processamento da saida de dados
    saidaDados(dic)

    

    # fim do programa princiaal

if __name__ == "__main__":
    main()