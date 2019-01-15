class Matriz:

    def __init__(self, linhas, colunas):
        self.elementos = self.gerarMatriz(linhas, colunas)


    def gerarMatriz(self, linhas, colunas):
        vetorExterno = []
        for k in range(linhas):
            for i in range(colunas):
                    vetorInterno = []
                    vetorInterno.append(-1)
                    vetorExterno.append(vetorInterno)
        return vetorExterno


    def inserirElemento(self, linha, coluna, ponto):
        self.elementos[linha].insert(coluna, ponto)
        ponto.setLinha(linha)
        ponto.setColuna(coluna)
