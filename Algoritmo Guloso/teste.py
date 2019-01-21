from matriz import Matriz
from ponto import Ponto
from caixeiroViajante import *
from datetime import datetime

matriz = Matriz(24)

ponto1 = Ponto('A')
ponto2 = Ponto('B')
ponto3 = Ponto('C')
ponto4 = Ponto('D')
ponto5 = Ponto('E')
ponto6 = Ponto('F')
ponto7 = Ponto('G')
ponto8 = Ponto('H')
ponto9 = Ponto('I')
ponto10 = Ponto('J')
ponto11 = Ponto('K')
ponto12 = Ponto('L')
ponto13 = Ponto('M')
ponto14 = Ponto('N')
ponto15 = Ponto('O')
ponto16 = Ponto('P')
ponto17 = Ponto('Q')
ponto18 = Ponto('R')
ponto19 = Ponto('S')
ponto20 = Ponto('T')
ponto21 = Ponto('U')
ponto22 = Ponto('V')
ponto23 = Ponto('X')
ponto24 = Ponto('Y')
ponto25 = Ponto('Z')
ponto26 = Ponto('Ô')
ponto27 = Ponto('Ã')
ponto28 = Ponto('Ê')
ponto29 = Ponto('Í')
ponto30 = Ponto('Á')
ponto31 = Ponto('Õ')
ponto32 = Ponto('Ó')
ponto33 = Ponto('Ẽ')
ponto34 = Ponto('Ý')
ponto35 = Ponto('Ŷ')

matriz.inserirElemento(0,14,ponto1)
matriz.inserirElemento(2,7,ponto2)
matriz.inserirElemento(3,0,ponto3)
matriz.inserirElemento(4,16,ponto4)
matriz.inserirElemento(4,8,ponto5)
matriz.inserirElemento(4,3,ponto6)
matriz.inserirElemento(4,1,ponto7)
matriz.inserirElemento(5,12,ponto8)
matriz.inserirElemento(5,21,ponto9)
matriz.inserirElemento(6,14,ponto10)
matriz.inserirElemento(7,14,ponto11)
matriz.inserirElemento(7,18,ponto12)
matriz.inserirElemento(8,14,ponto13)
matriz.inserirElemento(8,22,ponto14)
matriz.inserirElemento(9,9,ponto15)
matriz.inserirElemento(10,9,ponto16)
matriz.inserirElemento(10,19,ponto17)
matriz.inserirElemento(11,12,ponto18)
matriz.inserirElemento(11,0,ponto19)
matriz.inserirElemento(12,10,ponto20)
matriz.inserirElemento(14,22,ponto21)
matriz.inserirElemento(14,4,ponto22)
matriz.inserirElemento(17,21,ponto23)
matriz.inserirElemento(17,11,ponto24)
matriz.inserirElemento(18,15,ponto25)
matriz.inserirElemento(19,5,ponto26)
matriz.inserirElemento(19,17,ponto27)
matriz.inserirElemento(20,16,ponto28)
matriz.inserirElemento(20,6,ponto29)
matriz.inserirElemento(21,13,ponto30)
matriz.inserirElemento(21,4,ponto31)
matriz.inserirElemento(21,2,ponto32)
matriz.inserirElemento(22,12,ponto33)
matriz.inserirElemento(22,5,ponto34)
matriz.inserirElemento(23,20,ponto35)


# matriz.inserirElemento(0,0,ponto1)
# matriz.inserirElemento(6,1,ponto2)
# matriz.inserirElemento(3,2,ponto3)
# matriz.inserirElemento(2,5,ponto4)
# matriz.inserirElemento(7,6,ponto5)
# matriz.inserirElemento(1,7,ponto6)
# matriz.inserirElemento(4,8,ponto7)
# matriz.inserirElemento(5,3,ponto8)
# matriz.inserirElemento(8,4,ponto9)

print("Problema bitônico euclidiano do caixeiro-viajante:")
matriz.mostrarMatriz(matriz) #Print da matriz
print(" ")

# Registra o momento antes da execução do algoritmo
t0 = datetime.now()

resp = caixeiroViajante(matriz) #Realiza o caminho bitônico

# Registra o momento apos a execução do algoritmo
t1 = datetime.now()

# Calcula a o tempo de execucao em milissegundos da operacao
diff = t1 - t0
tempo = (diff.total_seconds() * 1000)

printArray(resp) #Print do caminho
print(" ")

# Exibe resultado do teste
print("Tempo de execução do Algoritmo Guloso: " + str(tempo) + " ms")
