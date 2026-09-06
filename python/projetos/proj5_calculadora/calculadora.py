#proejeto 5 - Calculadora

print (":::::::CALCULADORA SIMPLES:::::::")
valor1 = int(input("Digite o número: "))
operação = input("Digite a operação desejada (+, -, *, /, %, ^):")
while (operação!="+" 
       and operação!="-"
       and operação!="*"
       and operação!="/"
       and operação!="%"
       and operação!="^"
       ):
    operação = input("Operação inválida, escolha entre das disponíveis (+, -, *, /, %, ^): ")
valor2 = int(input("Digite outro número: "))
if (operação=="+"):
    resultado = valor1+valor2
    print("Resultado: ",resultado)
elif(operação=="-"):
    resultado = valor1-valor2
    print ("Resultado: ",resultado)
elif(operação=="*"):   
    resultado = valor1*valor2
    print ("Resultado: ",resultado)
elif(operação=="/"):   
    resultado = valor1/valor2
    print ("Resultado: ",resultado)
elif(operação=="%"):   
    resultado = valor1%valor2
    print ("Resultado: ",resultado)
else:
    resultado = valor1**valor2
    print ("Resultado: ",resultado)
print("Operação Finalizada")
