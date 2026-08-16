dicionario = {"RA":123,"Nome":"Alexandre","Idade":23,"AV1":7,"AV2":9}
# um dicionário é como uma lista, porém o seu índice é por chaves. Não se rastreia como em listas, ex : aluno [0]
# a chave(campo) possue um nome, e o seu valor | para rastrear o valor é apresentando o nome do dicionário, e o nome da chave.

print("Dicionário[RA]: ",dicionario["RA"])

dicionario["RA"] = 456
print ("Dicionário[RA] após atualização :" , dicionario["RA"])

print("*" * 75)

print("Chaves presentes no dicionário:")
for chaves in dicionario:
    print(chaves)
    
print("*" * 75)   

for chaves,valores in dicionario.items():  #cria duas variáveis demporárias, uma para guardar o nome do campo, e a segunda o valor contido dentro do campo
    # items() --> transforma o dicionário em uma lista de pares, entregando para o for a chave e o valor juntos.
    
    print(chaves,":",valores)
    
print("*" * 75)

if ("Idade" in dicionario):
    print("Idade: ",dicionario["Idade"])    

print("*" * 75)

if ("Alexandre" in dicionario.values()): # values() -> verifica apenas os valores dentro dos campos
    print("Alexandre é um valor que pertence ao dicionário")


print("*" * 75)
print("Dicionário Original: ",dicionario)    

del dicionario["Idade"] # del -> remove o campo informado
print("Dicionário após deletar Idade: ",dicionario)

#add nova chave. Chave média

print("*" * 75)

media = (dicionario["AV1"]+dicionario["AV2"])/2 # operação utilizando valores dos campos e salvando na variavel
dicionario["Média"] = media # cria nova chave(campo), com o valor da variável

print("Novo Dicionário: ", dicionario)
