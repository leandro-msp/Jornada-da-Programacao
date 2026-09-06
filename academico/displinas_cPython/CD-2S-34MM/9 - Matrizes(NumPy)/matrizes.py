import numpy as np  

matriz = np.array([[1,2,3],[4,5,6],[7,8,9],[10,20,30]]) # ao olharmos para uma matriz devemos imaginar cada bloco em uma linha , e formando colunas ->
# [1 2 3]
# [4 5 6]
# [7 8 9] ...
print("Matriz: ", matriz)

print("Elemento da posição(1,2): ",matriz[1][2]) #saída = 6
#explicação -> toda índice começa por 0, logo o primeiro argumento(posição) (1) é a segunda casa de elemtnos ([4,5,6])
# -> seguindo mesmo coneito o segundo argumento(posição) (2) é o número 6 -> pois 0=4, 1=5, 2=6

print("Dimensões: ", matriz.ndim)

matriz[3][1]=18 # alterando elemento da linha 3 e coluna 1 , respeitando os índices - > Linha 4 e Coluna 2 = 20 -> 18
print("Matriz Alterada: ",matriz)

#Operações matmáticas com Matrizes

matriz01 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,20,30]])
matriz02 = np.array([[2,2,2],[6,9,-10],[1,7,9],[3,6,8]])
matriz03 = np.array([[1,1],[0,4],[2,2]])

matrizsoma = matriz01+matriz02
matrizsub = matriz01-matriz02
matrizprod = matriz01.dot(matriz03)

print("Matriz 01:\n", matriz01)

print ("Matriz 02:\n ",matriz02)

print("Matriz 03: \n", matriz03)

print("Soma das Matrizes 01 e 02: \n", matrizsoma)

print("Subtração das Matrizes 01 e 02: \n",matrizsub)

print("Produto Matriz 01 x Matriz 03: \n",matrizprod)

