alunos = ["João","Ana","Maria"]
for x in alunos:
    print("Aluno: ",x)
    av1 = int(input("Insira nota da AV1: "))
    av2 = int(input("Insira nota da AV2: "))
    média = (av1+av2) / 2
    print("A média de ",x,"foi:" , média)
print("Operação Finalizada!")


# este método torna um pouco mais lento, pois teria que adicionar os nomes diratamente no código, e não na execução

