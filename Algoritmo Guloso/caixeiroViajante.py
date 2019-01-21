from matriz import Matriz
from ponto import Ponto


def resgatarPontos(matriz):
    retorno = []
    for k in range(matriz.linha):
        for i in range(matriz.coluna):
                if matriz.elementos[k][i] != -1:
                    retorno.append(matriz.elementos[k][i])
    return retorno

def ordenarPontosPorColuna(vetor):
    vetor.sort(key=lambda x:x.coluna)
    return vetor

def caixeiroViajante(matriz):
    pontos = resgatarPontos(matriz)
    pontos = ordenarPontosPorColuna(pontos)
    pontosAux = pontos[:]

    vetorAux = [pontos[0]]

    for k in range(0, (len(pontos)-2), 2):
        if pontos[k+1].linha <= pontos[k+2].linha:
            vetorAux.append(pontos[k+2])
            pontosAux.remove(pontos[k+2])
        else:
            vetorAux.append(pontos[k+1])
            pontosAux.remove(pontos[k+1])

    vetorAux.reverse()
    for k in range(len(vetorAux)):
        pontosAux.append(vetorAux[k])

    return pontosAux

def printArray(array):
    valor = []
    for k in range(len(array)):
        valor.append(array[k].nome)
    print(valor)
