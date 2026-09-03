print(":"*15,"DIC ANINHADO",":"*15)
# DICIONÁRIO ANINHADO

# É um dicionário composto por outro(s) dicionário(s)
dados = { 
    'games' : {"Rockstar":"GTA","Activision":"COD","EA":"Need For Speed"},
    'hardware' : {"Intel":"i914900k","AMD":"Ryzen 7 7800x3d","NVIDIA":"RTX 4090"},
    'perifericos' :{ "Logitech":"Mouse G703","Razer":"Cynosa","LG":"Monitor-Ultra Gear 180Hz"}

}
# dicionário competo 
print ("Dicionário completo:\n",dados)

# Recuperando Conteúdo de cada Dicionário "Games,Hardware e periféricos:"
print("\nConteúdo de cada dicionário(Games,Hardware e Periféricos:)")

for lista in dados.values(): # neste cenário o values hage/ atribui como valor, todo o conteúdo (chave:valor) de cada dicionário
   print(lista)

#recuperando somente as chaves de todas os dicionários(inviduais):
print("\n::::::::RECUPERANDO CHAVES::::::::")

print("\nChaves Individualmente:")
for lista in dados.values():
   #o conteúdo de cada dicionário será atribuído para variável lista, neste caso será chave:valor, por se tratar de aninhado, se fosse um simples, seria diretamente os valores
   for chave in lista:
      # será resgatado de dentro da varíavel lista as chaves, e atribuído a variável chave
      print (chave)

# Chaves de um dicinário específico
print ("\nChaves Dicionário Específico:")
chaves_hardware = dados['hardware'].keys() # método keys() identifica as chaves
   #a variável chaves_hardware conterá as chaves somente do dicionário 'hardware'
print (chaves_hardware)

#chaves individuais
for chave in dados['hardware']:
   # lê direramente o dicinário 'hardware' que está dentro de de dados, e os itens são atribuidos á variavel chave
   print (chave)
   # impressão individual de cada chave

#RECUPERANDO VALORES

print("\n::::::::RECUPERANDO CHAVES::::::::")
#Valor de Chave Específica

print ("\nValor de única chave:")
placaVideo = dados['hardware']['NVIDIA']
   #busca direta > varre o dicionário dados, e procura diretamente dentro do sub_dicionário 'hardware' a chave 'NVIDIA' e recupera o valor dentro desta chave
print ("Placa de Vídeo:",placaVideo)            

processador = dados['hardware']['AMD']
print ("Processador:",processador)

game = dados['games']['Activision']
print ("Jogo:",game)
   # o método direto é válido quando já se sabe quais chaves existem dentro do dicionário, caso seja feita uma busca de uma chave que não existe, resultará em erro(KeyError)

# Somente Valores
print("\nSomente os valores de todas as chaves de todos os sub-dicionários, individualmente:")
for lista in dados.values():
   #percore o dicionário dados, acessa os dados(chave:valor)de cada sub_dicionário('games','hardware','periféricos') e atribuiu a variável lista
   for produto in lista.values():
       #resgata os valores (de cada chave) dentro de lista e atribuiu á variável produto, ex.: 1ª os valores de de cada chave dentro de 'games', e assim por diante.
       print(produto)
   

#VERIFICAR SE CHAVE EXISTE
print("\n::::::::CHEGAR SE CHAVE EXISTE::::::::")

#métdo direto

chave_procurada = 'Logitech'

if chave_procurada in dados['perifericos']:
   print ("Chave Existe")
   # métodos que vai gerar erro caso a chave não existe dentro do dicionário

produto = dados['games'].get('Ubisoft','Não Cadastrado') # get() pega o valor dentro da chave
print (produto)

#valor da chave

print ("ITEM:")
chave_procurada = 'Logitech'
if chave_procurada in dados['perifericos']:
   item = dados['perifericos'][chave_procurada]
   print (item)

#ou
item = dados['perifericos'].get(chave_procurada)
if item:
   print(item)

