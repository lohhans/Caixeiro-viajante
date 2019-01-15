from matriz import Matriz
from ponto import Ponto

caixeiroViajante(matriz, pontoInicial):
    resultado = []
    laco = pontoInicial.coluna

    while laco <= len(matriz.elementos[0]):
        resultado.append(caixeiroViajanteIda(matriz, pontoInicial))
    while (pontoInicial.getNome in resultado) != false:
        resultado.append(caixeiroViajanteVolta(matriz, pontoInicial, resultado))

    return resultado

caixeiroViajanteIda(matriz, pontoInicial):
    for k in range(pontoInicial.coluna, len(matriz.elementos[0])):
        for i in range(pontoInicial.coluna, len(matriz.elementos[0])):
            if(matriz.elementos[k][i] != -1):
                return matriz.elementos[k][i].getNome

caixeiroViajanteVolta(matriz, pontoFinal, resultado):
    for k in range(pontoFinal.coluna, -1, -1):
        for i in range(pontoFinal.coluna, -1, -1):
            if(matriz.elementos[k][i] != -1) and (matriz.elementos[k][i].getNome in resultado == False):
                return matriz.elementos[k][i].getNome

mostrarResultado(resultado):
    final = ''
    for k in range(len(resultado)):
        final += str(resultado[k]) + '->'
    final = (final[0:(len(final)-2)])
    print(final)
