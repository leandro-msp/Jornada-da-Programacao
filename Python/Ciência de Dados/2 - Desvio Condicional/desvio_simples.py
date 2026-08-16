print("Exemplo 1 : ")
a = 5
b = 5
c = 2 
d = 0
if (a==b): #se A for igual a B // true
    c = a+b # o valor de C passa ser a soma de A e B (5+5)
    c = c+5 # C passa a valer seu novo valor + 5 (10 + 5)
d = c + 10 # D tem o valor de C + 10 (15+10)
print(d) # logo a saída será 25


print("Exemplo 2: ")
a = 5
b = 3
c = 2
d = 0
if (a==b): #false
    c = a+b # não será executado
    c = c+5 # não será executado
d = c + 10 # D vai valer C + 10 ( 2 + 10)
print(d) # 12

