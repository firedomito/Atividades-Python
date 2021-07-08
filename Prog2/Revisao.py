#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# ARQUIVO.py
#
# Copyright 2021
# Autor: Guilherme Silveira Mendes
#
############################
# Código fonte em Python 3
############################

def reposta(n):
    n = str(n)
    arm = ""
    for x in range(len(n)-1,-1,-1):
        arm = arm + n[x]
    arm = int(arm)
    return arm

def main():
    n = int(input())
    arm = reposta(n)
    print("N =", n, "->", "M =", arm)


if __name__ == "__main__":
    main()