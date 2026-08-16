#Uso do Laço for para calcular média de mais de um aluno.


qtde = int(input("Digite a quantidade de alunos: ")) # usuário já possui um valor fixo(definido) 
for(x) in range(0,qtde,1):  # o loop começa em zero | termina na quantidade o usuario inseriu | avança de um em um
    # o bloco inteiro abaixo será percorrido(irá se repetir) com base na qtdd que usuário
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Digite AV1: "))
    av2 = float(input("Digite AV2: "))
    média = (av1+av2) / 2
    print("A média do aluno ",aluno," foi: ", média)
print("Operação finalizada!")