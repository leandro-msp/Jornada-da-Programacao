import re

string = "O aluno José foi reprovado. A aluna Ana foi aprovada e os alunos Thiago e Andre ficaram em dependência"

procurar = re.match("O aluno", string) # o match procura o valor desejado no início da string
print(procurar)
procurar = re.match("Ana", string)
print(procurar) # ao retornar None, é pq nn foi encontrado o valor na posição informada(neste caso no início da string)
procurar = re.search("O aluno", string) # o serch procura na string inteira
print(procurar)
procurar = re.search("Ana", string)
print(procurar)
procurar = re.search ("Monica", string)
print(procurar)

#Raw String

print ("Leonardo\nFernanda")
print (r"Leonardo\nFernanda")

string = "O aluno José foi reprovado. Ele tirou 10 na segunda nota"
procurar = re.search(r"\w\w\w\w\w\w",string) #primeira ocorrência que tenham sequencia de 6 caracteres seguidos quer sejam número ou letras
if (procurar):
    print(procurar.group()) # mostra o valor recuperado
else:
    print("Não encontrado")

procurar = re.search(r"\d", string) # primeira ocorrencia que seu tenha caracetre numérico
if(procurar):
    print(procurar.group())
else:
    print ("Não encontrado")

procurar = re.search(r"\w\w\w\w\w\w+",string) # a ocorrência deve ter 6 caracteres ou mais, sendo alfanumérico
if (procurar):
    print(procurar.group())
else:
    print("Não encontrado")

procurar = re.search(r"\w{6,8}",string)  # ocorrencia alfanumérica com mínimo 6 me max 8 caracteres seguidos, sendo alfanumérico
if (procurar):
    print(procurar.group())
else:
    print("Não encontrado")
    
procurar = re.search(r"\w{5}\w+", string) # ocorrencia ao menos 6 caracteres , 5 do ja definido e mais um decorrente do w+
if (procurar):
    print(procurar.group())
else:
    print("Não encontrado")
    
procurar = re.search(r"\d+",string) # ocorrência com pelo menos 1 caractere numérico, podendo ser mais
if (procurar):
    print(procurar.group())
else:
    print("Não encontrado")
    
#caso tiver numero(nota com ponto) float :

procurar =  re.search(r"\d+\.\d+", string)
if (procurar):
    print(procurar.group())
else:
    procurar= re.search(r"\d+",string)
    if (procurar):
        print(procurar.group())
    else:
        print("Não encontrado")
string = "O aluno José foi reprovado. "

#Findall
# - > Procura várias ocorrências que satisfaçam a expressão regular e irá armazenar em uma lista.

string = "O aluno José foi reprovado. Ele tirou 7.7 na segunda nota"

procurar = re.findall(r"\w\w\w\w+", string)
if (procurar):
    for ocorrência in procurar:
        print(ocorrência)
else: print ("Não encontrado")