def leituraArq(entrada):
    #declaracao de variaveis
    dicionario = {}

    #Um processo de repetição que varre até a ultima palavra do arquivo
    while texto := entrada.readline():
        #Separador é um metodo utilizado para separar as palavras em uma lista
        separador = texto.split(';')
        dicionario[separador[0][8:].replace('"', '')] = [float(separador[1].replace(',', '.')), int(separador[2]), int(separador[3])]
    return dicionario

def saidaDados(dicionario):
    
    #Coloca os itens em ordem crescente
    dicionarioSort = sorted(dicionario.items(), key=lambda x: x[1])


    # escreve no arquivo saida.txt
    with open('saida.txt', 'w') as saida:
        for key, element in dicionarioSort:
            resultado = f'{key};{element[0]};{element[1]};{element[2]}'
            saida.write(resultado + '\n')

            #saida de dados
            print(resultado)

    return dicionarioSort

