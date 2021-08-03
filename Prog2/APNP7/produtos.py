import json

def separacao(entrada):
    #declaracao de variaveis
    produtos = {}

    #Um processo de repetição que varre até a ultima palavra do arquivo
    while texto := entrada.readline().strip():
        #Separador é um metodo utilizado para separar as palavras em uma lista
        separador = texto.split(';')
        produtos[separador[0]] = [float(separador[1]), int(separador[2]), int(separador[3])]
    return produtos


def consulta_estoque(nome_produto, produtos):
    if nome_produto not in produtos:
        print('PRODUTO INEXISTENTE.')
        return 0
    else:
        return nome_produto


def verifica_estoque(nome_produto, produtos, qtd_produto):
    qtd_usuario = qtd_produto

    qtd_estoque = produtos[nome_produto][1]
    qtd_vendido = produtos[nome_produto][2]


    qtd_estoque = (qtd_estoque - qtd_vendido)

    if qtd_usuario > qtd_estoque or qtd_usuario == 0:
        print("QUANTIDADE EM ESTOQUE INSUFICIENTE.")

    elif qtd_estoque >= qtd_usuario and qtd_usuario > 0:
        produtos[nome_produto][2] = (produtos[nome_produto][2] + qtd_usuario)
        print ("COMPRA REALIZADA COM SUCESSO")

    return qtd_vendido



def saida_dados(saida, produtos, ):
    #declaracao de variavel
    lst_produtos = []


    #Percorre o dicionario e adiciona o produtos ao dicionario
    for key in produtos:
        valor = (produtos[key][0] * produtos[key][2])
        lst_produtos.append(f'PRODUTO={key} VENDAS={valor:.2f}')

    with open('dados.json', 'w') as fp:
        json.dump(produtos, fp, indent=4)
        
    #Organiza em ordem alfabetica
    lst_produtos.sort()

    #Percorre por todos os produtos e printa o nome e preço dele
    for x in lst_produtos:
        print (x)
        saida.write(x + '\n')
