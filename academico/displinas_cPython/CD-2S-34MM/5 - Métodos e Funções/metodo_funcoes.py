'''
MÉTODOS E FUNÇÕES

> Quebra de problemas maiores e vários problemas menores(sub-problemas)
> cada sub/problema é solucionao e ao final tremos a solução do problema maior
'''
#FUNÇÃO
'''
 -> é um bloco de programa contendo início e fim e identificação por um nome,que será referenciado em 
 qualquer parte do programa principal ou em outra função.
 
 -> Retorna um valor ou variável para o programa que fez a chamada.
 
 -> Quando a chamada ela é executada até seu término e a execução do programa retorna exatamente para a primeira linha de instrução, 
 após a linha que fez a chmada da fução.
 
 -> Podem ter argumentos (parâmentros de entrada) ou não.
 -> Podem ou não retornar valor , as que não retornam valores são conhecidas como procedimento.
'''


'''SINTAXE DA CRIAÇÃO DE UM FUNÇÃO QUE NÃO RETORNA VALOR (PROCEDIMENTO):'''
#    def <nome da função> (<argumento_1>,<argumento_2>,argumento_3,<argumento_n>):
#        <instrução a ser executada pela função>

'''SINTAXE DA CRIAÇÃO DE UM FUNÇÃO QUE  RETORNA VALOR:'''
#    def <nome da função> (<argumento_1>,<argumento_2>,argumento_3,<argumento_n>):
#        <instrução a ser executada pela função>
#        return < valor a ser retornado pela função>


#Exemplo:

def fimprograma():
    mensagem = "Fim do Programa. Aula Método e Funções"
    return mensagem

def mostrarmensagem(nome,media):
    print("Seu nome é: ",nome," e sua média foi de: ",media)
    
def media(nota1,nota2):
    resposta =  (nota1+nota2)/2
    return resposta

def colecao(objcolecao):
    maiorvalor=0
    for x in objcolecao:
        if x > maiorvalor:
            maiorvalor = x
    return maiorvalor

n = input("Digite seu nome: ")
a =  float(input("Nota1: "))
b =  float(input("Nota2: "))
m = media(a,b)
mostrarmensagem(n,m)
print("Maior item da coleção: ",colecao([4,75,89,66]))
msg = fimprograma()
print(msg)


