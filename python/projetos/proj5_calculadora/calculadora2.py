#projeto 5 - calculadora 2 (match-case):

print (">>>> CALCULADORA SIMPLES <<<<")

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
    # while operação not in ["+", "-", "*", "/", "%", "^"]:
    # operação = input("Operação inválida, escolha entre as disponíveis (+, -, *, /, %, ^): ")
valor2 = int(input("Digite outro número: "))
match operação:
    case "+":
        resultado = valor1+valor2
        print("Resultado: ",resultado)

    case "-":
        resultado = valor1-valor2
        print ("Resultado: ",resultado)

    case "*":
        resultado = valor1*valor2
        print ("Resultado: ",resultado)
    case "/":
        resultado = valor1/valor2
        print ("Resultado: ",resultado)

    case "%":
        resultado = valor1%valor2
        print ("Resultado: ",resultado)
    case _: # default
        resultado = valor1**valor2
        print ("Resultado: ",resultado)
print("Operação Finalizada")