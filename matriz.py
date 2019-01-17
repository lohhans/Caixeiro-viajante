class Matriz:

    def __init__(self, tamanho):
        self.elementos = self.gerarMatriz(tamanho, tamanho)
        self.linha = tamanho
        self.coluna = tamanho

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

    def mostrarMatriz(self, matriz):
        linhas = matriz.linha
        colunas = matriz.coluna
        matrizP = ''
        for k in range(linhas):
            linha = ""
            for i in range(colunas):
                elemento = matriz.elementos[k][i]
                if elemento == -1:
                    linha += " . "
                else:
                    linha += " "+elemento.nome+" "
            matrizP += linha+"\n"
        print(matrizP)

    def mostrarMatrizColuna(self, matriz):
        linhas = matriz.linha
        colunas = matriz.coluna
        matrizP = ''
        for k in range(linhas):
            linha = ""
            for i in range(colunas):
                elemento = matriz.elementos[i][k]
                if elemento == -1:
                    linha += " . "
                else:
                    linha += " "+elemento.nome+" "
            matrizP += linha+"\n"
        print(matrizP)

    def getLinha(self):
        return self.linha

    def getColuna(self):
        return self.coluna
