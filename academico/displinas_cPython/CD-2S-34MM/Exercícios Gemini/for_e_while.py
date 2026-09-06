# Desafio 1: O Somador (Usando for)
""" 
    Crie um programa que calcule a soma de todos os números de 1 até 10.

Dica: Crie uma variável chamada soma = 0 antes do loop e, dentro do for, vá somando o número atual a ela.

Resultado esperado: O programa deve imprimir o valor final (que é 55).
    """

soma = 0
for numero in range(1,11):
    soma = soma + numero
    print(f"Somando {numero}... Total parcial: {soma}")
print ("Resultado : " , soma)
    

# Desafio 2: A Bomba Relógio (Usando while)
"""Crie uma contagem regressiva que começa em 10 e vai até 0.

Regra: O programa deve imprimir cada número e, quando chegar no 0, deve imprimir "BOOOOM! 💥".

Dica: Lembre-se de diminuir o valor da variável a cada volta do loop (contador -= 1).
    """
    
contador = 10
while contador >= 0:
    print (f"Contagem Regressiva: {contador} ")
    contador -=1
print ("BOOOOM!!")
    
    

