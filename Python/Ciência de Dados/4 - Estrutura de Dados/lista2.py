aluno = ['Leonardo','Ricardo','Monica','Fernanda','Luiza']
print("Lista alunos no ponto incial :\n", aluno)

aluno.append("João") # append -> adiciona novo elemebnto no final da lista
print("Lista após add 'João' no final :\n", aluno)

aluno.insert(2,"Gilberto") #insert -> adiciona novo elemento em um índice(posição) específica, sem deletar o atual dado dessa posição
print("Lista após inserir 'Gilberto' no índice 2 , ou seja posição 3: \n", aluno)

aluno.remove("Ricardo") # remove -> deleta da lista o dado informado.
print("Lista após remover 'Ricardo' dos elementos: \n" , aluno)

aluno[4] = "Leonardo" # altera/atualiza o valor do índice informado
print("Lista após adicionar Leonardo no índice 4 \n", aluno)

contador = aluno.count("Leonardo") # count --> conta a quantas vezes um elemento específico aparece em uma lista, string ou tuplas (frequência de um elemento)
print("Quantidade de alunos que possuem o nome 'Leonardo' :", contador)
print("Quantidade de itens que tem dentro da lista aluno: ", len(aluno)) # len --> conta a quantidade(total) de elementos
aluno.sort() # sort --> organiza em ordem alfabética/numérica 
print("Lista de alunos após a ordenação \n", aluno)
if "Leonardo" in aluno: # in -> verifica se o elemento está presente, e retorna verdadeiro ou falso
    print("Este aluno pertence a lista.")
if "Kaique" not in aluno: # not in -> verifica se o elemento não está presente, e retonar verdadeiro ou falso
    print("Este aluno não pertence a lista.")