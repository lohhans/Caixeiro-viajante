class Matriz:

    def __init__(self, linhas, colunas):
        self.elementos = self.gerarMatriz(linhas, colunas)
        self.linha = linhas
        self.coluna = colunas

    def gerarMatriz(self, linhas, colunas):
        vetorExterno = []
        for k in range(linhas):
            vetorInterno = []
            for i in range(colunas):
                vetorInterno.append(-1)
            vetorExterno.append(vetorInterno)
        return vetorExterno

    def inserirElemento(self, linha, coluna, ponto):
        self.elementos[linha][coluna] = ponto
        ponto.setLinha(linha)
        ponto.setColuna(coluna)

    def mostrarMatriz(self, matriz, linhas, colunas):
        matrizP = ''
        for k in range(linhas):
            linha = ""
            for i in range(colunas):
                elemento = matriz.elementos[k][i]
                if elemento == -1:
                    linha += " -1 "
                else:
                    linha += "  "+elemento.nome+" "
            matrizP += linha+"\n"

        print(matrizP)
