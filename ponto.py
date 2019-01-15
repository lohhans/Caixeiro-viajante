class Ponto:

    def __init__(self, nome):
        self.nome = nome
        self.linha = -1
        self.coluna = -1

    def inserirCordenadas(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna


    def inserirElemento(self, linha, coluna, elemento):
        self.elementos[linha].insert(coluna, elemento)

    def getNome(self):
        return self.nome

    def setLinha(self, linha):
        self.linha = linha

    def setColuna(self,coluna):
        self.coluna = coluna
