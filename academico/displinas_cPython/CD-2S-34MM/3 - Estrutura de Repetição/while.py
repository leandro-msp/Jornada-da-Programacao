
repetir = "s"
while(repetir=="s"):
    print("Cálculo de Média:")
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Insira sua nota da av1: "))
    av2 = float(input("Insira sua nota da av2: "))
    média = (av1+av2) / 2
    print ("A média do Aluno", aluno, "foi: ", média)
    repetir = input("Caso queira calcular nova média, digite 's', caso contrário digite: 'n' : ")
print("Fim da operação!!")



