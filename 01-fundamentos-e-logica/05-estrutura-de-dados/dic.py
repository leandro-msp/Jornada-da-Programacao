estudo= {"Curso":"ADS","Disciplina":"Ciência de Dados","Linguagem":"Python"} # compostor por chave,valor , sendo que a chave é o index

print ("::::::::DICIONÁRIO COMPLETO::::::::\n" 
       ,estudo)

# RESGATANDO SOMENTE AS CHAVES
print("::::::::CHAVES NO DICIONÁRIO::::::::")


for chave in estudo:
    print (chave)
    
# RECUPERANDO VALORES 
print ("::::::::VALORES DAS CHAVES::::::::")

#opção1
print ("Recuperando pelo índice:\n",
       estudo["Curso"]) # resgatando valor através da chave

#opção2
print ("Método simples:")

valores = estudo.values()
print(valores)

#opção3
print ("\nUtilizando o FOR:")

for valor in estudo.values(): # método values() extrai somente os valores dentro das chaves:
    print (valor)

#RECUPERANDO CHAVE E VALOR
print ("::::::::CHAVE/VALOR::::::::")

#opção1
print ("SIMPLES:")

#opção2
chaveValor= estudo.items()
print(chaveValor)

#opção3
print ("\nUtilizando o FOR:")

for chave,valor in estudo.items(): # o método items() retorna pares de chave-valor.
    print (chave,":",valor)




