print("Exemplo 1 : ")
a=5
b=3
c=2
d=0
if (a==b):
    c = a+b
    c = c + 5
d = c + 10
print(d)

#SEM IDENTAÇÃO  
print("Exemplo 2: ")
a=5
b=3
c=2
d=0
if (a==b):
    c = a+b
c = c + 5 # deixou de fazer parte do trecho a ser executado caso a afirmação fosse verdadeira, ou seja será executado idenpendentemente 
d = c + 10
print(d)

