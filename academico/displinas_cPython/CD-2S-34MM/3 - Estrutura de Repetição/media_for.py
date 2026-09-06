qtde = int(input("Digite a quantidade de alunos: "))
for(x) in range(0,qtde,1):
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Digite AV1: "))
    av2 = float(input("Digite AV2: "))
    média = (av1+av2) / 2
    print("A média do aluno ",aluno," foi: ", média)
print("Operação finalizada!")