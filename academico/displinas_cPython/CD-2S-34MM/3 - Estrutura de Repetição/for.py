for x in range(2,17,3): #primiero parâmetro é onde inicia , segundo parâmetro onde ele para, e terceiro o intervalo entre os números
    print(x)
    

print("Exemplo 2 :")
for x in range(5): # por padrão começa em zero, e intervalo de um. Onde para sempre será obrigatório
    print(x)
    

print("Exemplo 3 :")

for x in range(1,6):
    print(x)
    
    
print("Exemplo 4 :")
for x in range(0,10,2):
    print(x)
    
print("Exemplo 5 :")
for x in range(5,0,-1): #passo negativo/ contagem regressiva
    print(x)




qtde = int(input("Digite a quantidade de alunos: "))
for x in range(0,qtde,1):
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Digite AV1: "))
    av2 = float(input("Digite AV2: "))
    média = (av1+av2) / 2
    print("A média do aluno ",aluno," foi: ", média)
print("Operação finalizada!")

    
    
