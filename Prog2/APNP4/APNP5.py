#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# APNP5.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################

#Import modularizado
from produtos import *

#Função Principal
def main():
    nome_entrada = input()
    nome_saida = input()


    #Leitura de arquivos
    entrada = open(nome_entrada, 'rt')
    saida = open(nome_saida, 'wt')

    #Entrada de dados
    nome_produto = input()
    
    produtos = separacao(entrada)

    while nome_produto != "FIM":
        qtd_produto = int(input())
        if consulta_estoque(nome_produto, produtos):
            verifica_estoque(nome_produto, produtos, qtd_produto) 
        nome_produto = input()


    saida_dados(saida, produtos)
    
    #Fechamento de arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    main()