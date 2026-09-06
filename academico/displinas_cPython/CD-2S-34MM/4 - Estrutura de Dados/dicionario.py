dicionario = {"RA":123,"Nome":"Alexandre","Idade":23,"AV1":7,"AV2":9}
print("Dicionário[RA]: ",dicionario["RA"])

dicionario["RA"] = 456
print ("Dicionário[RA] após atualização :" , dicionario["RA"])

print("*" * 75)

for chaves in dicionario:
    print(chaves)
    
print("*" * 75)   

for chaves,valores in dicionario.items():  # for x,y in dicionario.items()
    print(chaves,":",valores)
    
print("*" * 75)

if ("Idade" in dicionario):
    print("Idade: ",dicionario["Idade"])    

print("*" * 75)

if ("Alexandre" in dicionario.values()):
    print("Alexandre é um valor que pertence ao dicionário")


print("*" * 75)
print("Dicionário Original: ",dicionario)    

del dicionario["Idade"]
print("Dicionário após deletar Idade: ",dicionario)

#add nova chave. Chave média

print("*" * 75)

media = (dicionario["AV1"]+dicionario["AV2"])/2
dicionario["Média"] = media

print("Novo Dicionário: ", dicionario)
