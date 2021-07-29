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


def modulo(curso):

    inscritos = 0
    dadosConc = {}

    while(curso) > 0:
        vagas = int(input())
        qtdFem = int(input())
        qtdMasc = int(input())

        totalCand = (qtdFem + qtdMasc)

        candVaga = (totalCand / vagas)

        porcentoFem = (qtdFem/totalCand)*100    

        dadosConc[curso] = [vagas, qtdMasc, qtdFem, candVaga, porcentoFem]


        inscritos += totalCand

        curso = int(input())
    
    maiorCandVagas = [0,0]

    for key in dadosConc:

        numCandVagas = dadosConc[key][3]

        if numCandVagas > maiorCandVagas[1]:
            maiorCandVagas = [key,numCandVagas]

        print(f'Curso={key} CV={numCandVagas:.2f} Perc Inscritos Feminino={dadosConc[key][4]:.2f}%')

    print(f'Maior Candidatos/Vagas={maiorCandVagas[1]:.2f} foi no curso={maiorCandVagas[0]}')
    print(f'Total de inscritos={inscritos}')
        

def main():

    curso = int(input())

    if curso > 0: 
        modulo(curso)



if __name__ == "__main__":
    main()