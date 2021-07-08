espaco = " "
caracter = "*"
opcao = "a"
espacamento = 6
a = ''
resultado = ''

if opcao == "a":
    for i in range(espacamento):
        print(str(caracter)*espacamento)


elif opcao=="b":
    for i in range(espacamento):
         a = print(str(caracter)*(i+1))  

elif opcao=="c":
    for i in range(espacamento, 0, -1):
        for j in range(7):
            if i > 5:
                resultado += str(espaco) * (i-j) + str(caracter) * j + "\n"


elif opcao=="d":
    k = 1
    n= 4
    for i in range(n, 0, -1):
        resultado += str(espaco) * (i-1) + str(caracter) * (k) + "\n"
        k += 2
    k = 5
    for j in range(1, n):
        resultado += str(espaco) * (j) + str(caracter) * (k) + "\n"
        k -= 2


elif opcao=="e":
    for i in range(n, 0, -1):
        resultado += str(caracter) * i + "\n"

elif opcao == "f":



print (resultado)