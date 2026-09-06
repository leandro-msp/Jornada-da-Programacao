#Limitando o Usuário, permitando apenas "s" ou "n" no final do "formulário".

# Adicionado fator de feedback conforme a média.

repetir = "s"               
while(repetir=="s"):        
    print("Cálculo de Média:")
    aluno = input("Digite o nome do Aluno: ")
    av1 = float(input("Insira sua nota da av1: "))
    av2 = float(input("Insira sua nota da av2: "))
    média = (av1+av2) / 2
    
    if (média<6):
        print(f"A média do aluno {aluno} foi: {média}, infelizmente está reprovado!")
    elif(média>=6 and média<=7):
        print(f"A média do {aluno} foi: {média}, está aprovado, mas pode melhorar! ")
    else:
        print(f"A média do {aluno} foi: {média}. Aprovadíssimo!")
    
    repetir = input("Caso queira calcular nova média, digite 's', caso contrário digite: 'n' : ")
    while (repetir!="s" and repetir!="n"):
        repetir = input("Comando não aceito, digite somente 's' ou 'n'!:")
        
print("Fim da operação!!")