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

    resultadoParcial = [pontos[0]]
    consicaoInverter = (len(pontos)-4)

    for k in range(0, (len(pontos)-4), 2):
        if pontos[k+1].linha <= pontos[k+2].linha:
            resultadoParcial.append(pontos[k+2])
            pontos.remove(pontos[k+2])

        else:
            resultadoParcial.append(pontos[k+1])
            pontos.remove(pontos[k+1])

    pontos = ordenarPontosPorColuna(pontos)
    resultadoParcial.reverse()
    for k in range(len(resultadoParcial)):
        pontos.append(resultadoParcial[k])

    if consicaoInverter < 0:
        pontos.reverse()

    return pontos

def printArray(array):
    valor = []
    for k in range(len(array)):
        valor.append(array[k].nome)
    print(valor)
