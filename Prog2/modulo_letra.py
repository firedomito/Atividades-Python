#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# modulo_letra.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################


#Todas funções abaixo fazem e retornam os padrões pedidos
def opc_a(caracter):
    #declaracao de variavel
    resultado = ''
    largura = 6

    for i in range(largura):
        resultado += (str(caracter)*largura) + "\n"
    return resultado

def opc_b(caracter):
    #declaracao de variavel
    resultado = ''
    largura = 6

    for i in range(largura):
        resultado += (str(caracter)*(i+1)) + "\n"
    return resultado
    

def opc_c(caracter):
    #declaracao de variavel
    resultado = ''
    largura = 6
    espaco_branco = ' '

    for i in range(largura, 0, -1):
        for j in range(7):
            if i > 5:
                resultado += str(espaco_branco) * (i-j) + str(caracter) * j + "\n"
    return resultado

def opc_d(caracter):
    #declaracao de variavel
    conta_caracter = 1
    largura = 4
    resultado = ''
    espaco_branco = ' '

    for i in range(largura, 0, -1):
        resultado += str(espaco_branco) * (i-1) + str(caracter) * (conta_caracter) + "\n"
        conta_caracter += 2

    if conta_caracter >= 9:
        conta_caracter = 5

        for j in range(1, largura):
            resultado += str(espaco_branco) * (j) + str(caracter) * (conta_caracter) + "\n"
            conta_caracter -= 2
    return resultado

    
def opc_e(caracter):
    #declaracao de variavel
    resultado = ''
    num_repeticao = 6

    for i in range(num_repeticao, 0, -1):
        resultado += str(caracter) * i + "\n"
    return resultado


def opc_f(caracter):
    #declaracao de variavel
    resultado = ''
    quant_carcter = 6
    num_repeticao = 7
    espaco_branco = ' '

    for i in range(1, num_repeticao):
        resultado += str(espaco_branco) * (i-1) + str(caracter) * (quant_carcter) + "\n"
        quant_carcter -= 1
    return resultado


