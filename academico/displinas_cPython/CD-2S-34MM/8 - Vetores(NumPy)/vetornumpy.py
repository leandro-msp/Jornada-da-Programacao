import numpy as np

#Exemplo de um vetor NumPy

vetor = np.array([8,34,67,98])

#imprimindo dados do vetor

print(vetor)
print ("Shape: ", vetor.shape) # informa a qtdd de colunas de um vetor
print("Dtype: ", vetor.dtype) # indica qual o tipo de dado dos valors armzds no vetor
print("Size: ",vetor.size) # retona a qtdd de elemtnos do vetor e/ou matriz
print ("Itemsize: ", vetor.itemsize) # retorna o tamanho de um elemento da matriz em bytes
print ("Ndim: ", vetor.ndim) # retorna o numero de dimensões da matriz

vetor2 =  np.array([8.87,34,67.89,98,1.09])

print(vetor2)
print ("Shape: ", vetor2.shape) 
print("Dtype: ", vetor2.dtype) 
print("Size: ",vetor2.size) 
print ("Itemsize: ", vetor2.itemsize) 
print ("Ndim: ", vetor2.ndim)

#Acessando e Alterando vetores

vetor3 = np.array([8,34,67,98])

print("Vetor inicial", vetor3)

print("Vetor posição 0: ",vetor3[0])
print("Vetor posição 2: ", vetor3[2])
vetor3[1]=231
vetor3[3]=105
print("Vetor com alterações realizadas \n",vetor3)


#Criação de Vetores
vetor4 = np.empty(10,int)
print ("Vetor 4: ",vetor4)

vetor5= np.zeros(10)
print("Vetor 5: ",vetor5)

vetor6 = np.ones(10)
print("Vetor 6: ",vetor6)

vetor7=np.arange(3,13,2,float)
print("Vetor 7: ",vetor7)

vetor8 = 6*np.random.random(5)
print("Vetor 8: ", vetor8)
