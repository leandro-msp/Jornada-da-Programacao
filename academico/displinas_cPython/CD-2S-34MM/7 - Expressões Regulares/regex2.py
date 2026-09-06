import requests
import re


requisicao = requests.post("https://www.terabyteshop.com.br/Central/MeusPedidos.obj?id=7036880")
string_retorno = requisicao.text

padrao = re.findall(r"\w{6,7}",string_retorno)
for ocorrência in padrao:
    print(ocorrência)
    comprimento = len(ocorrência)
    print (ocorrência[7:comprimento])
