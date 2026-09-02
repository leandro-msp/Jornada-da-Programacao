aluno = ['Leonardo','Ricardo','Monica','Fernanda','Luiza']
time2 = ['Gremio','São Paulo','Palmeiras','Santos','Corinthians']
curso = [] # lista vazia
notas = [0,1,2,3,4,5,6,7,8,9,10]

print (aluno[0])
print (aluno[2])
print (aluno[4])

print ("*" * 80)

for alunoaux in aluno: # para cada elemento na lista (variavel aluno), atribui em alunoaux
    print(alunoaux)
    
print("*" * 80)
    
import json  #biblicoteca para uso das funções JSON 

with open ('lista.json','r') as listas: # with open --> abre e fechar lista automaticamente | 'r" --> significa "read(ler)" | as --> cria uma apelido para usar o arquivo que foi aberto
    dados = json.load(listas) # lê as informações de dentro do arquivo(lista) e salva-os na variável(dados)
    print(dados)
    
print("*" * 80)

for item in dados["curso"]: # atrubuir na variável 'item' cada elemento presente em 'dados' cujo pertecem a lista "curso".
    print(item)
    
    