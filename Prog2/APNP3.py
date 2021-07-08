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

#Import do arquivo que faz as opções
from modulo_letra import *

def main():
    #Lista de opções
    opcao = ["a", "b", "c", "d", "e", "f"]

    #Declaração de Variaveis
    resultado = ''

    #Entrada de dados
    opcao_letra = input()

    #Processamento
    while opcao_letra in opcao:
        caracter = input()
        if opcao_letra == opcao[0]:
            resultado +=  (opc_a(caracter))
            #Saida de dados

        elif opcao_letra == opcao[1]:
            resultado += (opc_b(caracter))
            #Saida de dados

        elif opcao_letra == opcao[2]:
            resultado += (opc_c(caracter))
            #Saida de dados

        elif opcao_letra == opcao[3]:
            resultado += (opc_d(caracter))
            #Saida de dados
        
        elif opcao_letra == opcao[4]:
            resultado += (opc_e(caracter))
            #Saida de dados

        elif opcao_letra == opcao[5]:
            resultado += (opc_f(caracter))
            #Saida de dados     

        opcao_letra = input()
    print(resultado)

if __name__ == "__main__":
    main()

#fim