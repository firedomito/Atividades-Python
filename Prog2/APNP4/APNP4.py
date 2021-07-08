#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# APNP4.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################

#Import modularizado
from modulo import modulo

#Função Principal
def main():

    #Entrada de dados
    nome_entrada = input()
    nome_saida = input()


    #Leitura de arquivos
    entrada = open(nome_entrada, 'rt')
    saida = open(nome_saida, 'wt')

    
    #Retorno da função modularizada
    resposta = modulo(entrada, saida)


    #Fechamento de arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    main()