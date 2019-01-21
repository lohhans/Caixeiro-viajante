from matriz import Matriz
from ponto import Ponto

def resgatarPontos(matriz):
    retorno = []
    for k in range(matriz.linha):
        for i in range(matriz.coluna):
                if matriz.elementos[i][k] != -1:
                    retorno.append(matriz.elementos[i][k])
    return retorno

def eliminarIntersecao(lista1, lista2):
    for i in range(len(lista2)):
        if lista2[i] in lista1:
            lista1.remove(lista2[i])
    return lista1


def caixeiroViajanteBT(matriz):
    pontos = resgatarPontos(matriz)
    caminho = []

    caminho.append(pontos[0])
    caminho[0].verificado = True
    # for k in range(len(pontos))

    i = 0
    k = 1

    while len(caminho) != len(pontos) and k < len(pontos):
        i += 1
        caminho.append(pontos[k])

        # print(caminho[i-1].nome + ' ' +str(caminho[i-1].linha))
        # print(pontos[k].nome+ ' ' +str(pontos[k].linha))

        if caminho[i-1].linha > pontos[k].linha and (caminho[i-1].verificado == False):

            caminho[i].verificado = True
            caminho.remove(caminho[i-1])
            k += 1
            i -= 1



        else:

            if k < len(pontos):
                k += 1

    pontos = eliminarIntersecao(pontos, caminho)
    pontos.reverse()

    for k in range(len(pontos)):
        caminho.append(pontos[k])

    return caminho

def printArray(array):
    valor = []
    for k in range(len(array)):
        valor.append(array[k].nome)
        # valor.append(array[k])
    print(valor)
