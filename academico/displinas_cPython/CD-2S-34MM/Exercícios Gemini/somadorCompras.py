from datetime import datetime
print("SOMADOR DE PREÇOS")

total = 0 
valor = -1


while valor !=0:
    valor = float(input("Digite o preço do produto (ou 0 para encerrar): "))
    total += valor
    print (f"O subtotal da compra é : R${total:.2f}")
cpf_solic =(input("Deseja informa o CPF? (S) ou (N) : "))
while (cpf_solic != "S" and cpf_solic !="N"):
    cpf_solic =(input("Deseja informa o CPF? (S) ou (N) : "))
if cpf_solic =="S":
    cpf = input("Digite o CPF: ")
    while len(cpf) !=11:
        print("Erro! o CPF precisa ter 11 dígitos.")
        cpf = input("Digite o CPF novamente: ")
else: 
    cpf = ""
print ("*" *25)
print(f"COMPRA FINALIZADA, O TOTAL A PAGAR É : R${total:.2f}")
if cpf!="":
    print(f"CPF DO CONSUMIRDOR:{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} ") 
hora = datetime.now()
print(f"Data e hora: {hora.strftime('%d/%m/%Y %H:%M:%S')} ")
print("-----VOLTE SEMPRE-----")

