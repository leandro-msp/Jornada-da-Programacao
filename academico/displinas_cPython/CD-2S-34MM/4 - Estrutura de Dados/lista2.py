aluno = ['Leonardo','Ricardo','Monica','Fernanda','Luiza']
print("Lista alunos no ponto incial :\n", aluno)

aluno.append("João")
print("Lista após add 'João' no final :\n", aluno)

aluno.insert(2,"Gilberto")
print("Lista após inserir 'Gilberto' no índice 2 , ou seja posição 3: \n", aluno)

aluno.remove("Ricardo")
print("Lista após remover 'Ricardo' dos elementos: \n" , aluno)

aluno[4] = "Leonardo"
print("Lista após adicionar Leonardo no índice 4 \n", aluno)

contador = aluno.count("Leonardo")
print("Quantidade de alunos que possuem o nome 'Leonardo' :", contador)
print("Quantidade de itens que tem dentro da lista aluno: ", len(aluno))
aluno.sort()
print("Lista de alunos após a ordenação \n", aluno)
if "Leonardo" in aluno:
    print("Este aluno pertence a lista.")
if "Kaique" not in aluno:
    print("Este aluno não pertence a lista.")