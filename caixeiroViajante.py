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

def gerarCaminho(matriz):
    pontos = resgatarPontos(matriz)
    pontos = ordenarPontosPorColuna(pontos)

    resultado = [pontos[0]]
    for k in range(0, (len(pontos)-3), 2):
        if pontos[k+1].linha < pontos[k+2].linha:
            resultado.append(pontos[k+2])
            del(pontos[k+2])

        else:
            resultado.append(pontos[k+1])
            del(pontos[k+1])

    pontos = ordenarPontosPorColuna(pontos)
    pontos.reverse()
    for k in range(len(pontos)):
        resultado.append(pontos[k])
    resultado.reverse()

    return resultado

def printArray(array):
    valor = []
    for k in range(len(array)):
        valor.append(array[k].nome + " "+str(array[k].coluna))
    print(valor)
