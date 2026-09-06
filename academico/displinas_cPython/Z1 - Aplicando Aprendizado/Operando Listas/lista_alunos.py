#1 - criar lista
alunos = []

#ATIVAR O LOOPING
continuar = "s"

#2 - inserir novo aluno
while (continuar=="s"):
    ra = int(input("Digite o RA do aluno: "))
    nome = input("Digite o nome do Aluno: ")
    curso = input("Digite o nome do Curso: ")
    nota1 = int(input("Digite a nota da AV1: "))
    nota2 = int(input("Digite a nota da AV2:"))
    média = (nota1+nota2)/2
    
#3 - Add dados na lista
    novo_aluno ={
        "RA": ra,
        "Nome": nome,
        "Curso": curso,
        "AV1": nota1,
        "AV2": nota2,
        "Média": média
    }
    alunos.append(novo_aluno)
       
#4 - Inserir mais alunos ou não
    continuar=input("Caso deseja adicionar um novo aluno digite 's', caso contrário 'n': ").lower()
    while continuar!="s" and continuar!="n":
        continuar=input("Comando inválido, digite apenas 's' ou 'n':")
    
#5 - contar qnts itens na lista, para conjulgação do texto conforme a quantidade        
contador=len(alunos)
if contador ==1:
    print("Aluno Cadastrado com Sucesso!!")
else:print("Alunos Cadastrados com Sucesso!!")


#6 - Exibir a lista

print("ALUNOS\n",":"*30) 

for cadastros in alunos:
    print(f"RA: {cadastros['RA']} |Aluno: {cadastros['Nome']} | Curso: {cadastros['Curso']} | AV1: {cadastros['AV1']} | AV2: {cadastros['AV2']} | Média: {cadastros['Média']}")

#7 - Filtrar alunos
for aluno in alunos:
    if aluno['Média']<6:
        print(":::::::ALUNOS REPROVADOS::::::")
        print(f"RA: {aluno['RA']} |Aluno: {aluno['Nome']} | Média: {aluno['Média']}")
