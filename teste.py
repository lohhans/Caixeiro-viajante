from matriz import Matriz
from ponto import Ponto
import caixeiroViajante

matriz = Matriz(5,5)

ponto1 = Ponto('A')
ponto2 = Ponto('B')
ponto3 = Ponto('C')
ponto4 = Ponto('D')
ponto5 = Ponto('E')
ponto6 = Ponto('F')
ponto7 = Ponto('G')

matriz.inserirElemento(0,1,ponto1)
matriz.inserirElemento(2,2,ponto2)
matriz.inserirElemento(2,3,ponto3)
matriz.inserirElemento(3,3,ponto4)
matriz.inserirElemento(3,4,ponto5)
matriz.inserirElemento(4,2,ponto6)
matriz.inserirElemento(3,0,ponto7)

resultado = caixeiroViajante(matriz, ponto2)
mostrarResultado(resultado)
