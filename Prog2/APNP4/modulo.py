def modulo(entrada, saida):
    #declaracao de variaveis
    livros = {}
    produto = []

    #Um processo de repetição que varre até a ultima palavra do arquivo
    while texto := entrada.readline().strip():
        #Separador é um metodo utilizado para separar as palavras em uma lista
        separador = texto.split(';')
        livros[separador[0]] = separador[1:]

    #Percorre o dicionario e adiciona o produto ao dicionario
    for key in livros.keys():
        produto.append(key)

    #Organiza em ordem alfabetica
    produto.sort()

    #Percorre por todos os produtos e printa o nome e preço dele
    for key in produto:
        resposta = f'PRODUTO={key} PRECO={livros[key]}'
        print (resposta)
        saida.write(resposta + '\n')