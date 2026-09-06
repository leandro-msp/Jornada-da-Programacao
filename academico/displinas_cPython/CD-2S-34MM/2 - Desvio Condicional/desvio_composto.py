a = 5 
b = int(input("Informe o valor de b: "))

c = 2 
d = 0 
if (a==b): # exemplo se B for 5
    c = a + b # C = 10
    c = c + 3 # C = 13 (10 + 3)
else: # exemplo se B for 3
    c = a-b  #C = 2
    c = c + 2 #C = 4 (2 + 2)
d = c + 10 #Caso true D= 23 (C(13)+10), Caso False D = 14  (C +10 (4+10))
print(d)

