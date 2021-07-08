#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# ParImpar.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################


# Função que verifica se a entrada é par ou impar
def VerfNum (n):
    if n % 2 == 0:
        return True
    else:
        return False


# Função Principal
def main():
   # Declaração de Variaveis
    n = int()
    verifica = 0

    # Entrada de dados
    n = int(input())

   # Processamento
    verifica = VerfNum(n)

    # Saida de dados
    if  verifica == True :
        print ("N =", n, "EH PAR")
    else:
        print ("N =", n, "EH IMPAR")

    # FIM

if __name__ == "__main__":
    main()