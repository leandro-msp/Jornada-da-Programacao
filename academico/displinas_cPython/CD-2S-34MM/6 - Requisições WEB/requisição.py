import requests
requisicao = requests.post("https://putsreq.com/t0aCL39Mz30NrWwMGIt8")
print(requisicao.text)
nome = input("informe seu nome: ")
requisicao = requests.post("https://putsreq.com/a6ZnhxrdUGZJnuXcMzVg?name="+nome)
print(requisicao.text)