aluno = ['Leonardo','Ricardo','Monica','Fernanda','Luiza']
time2 = ['Gremio','São Paulo','Palmeiras','Santos','Corinthians']
curso = []
notas = [0,1,2,3,4,5,6,7,8,9,10]

print (aluno[0])
print (aluno[2])
print (aluno[4])

print ("*" * 80)

aluno = ['Leonardo','Ricardo','Monica','Fernanda','Luiza']
for alunoaux in aluno:
    print(alunoaux)
    
print("*" * 80)
    
import json

with open ('4 - Estrutura de Dados/lista.json','r') as arquivo:
    dados = json.load(arquivo)
    print(dados)
    
print("*" * 80)

for item in dados["curso"]:
    print(item)
    
    