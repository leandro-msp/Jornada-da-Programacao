from aluno import AlunoEL
 
aluno1 = AlunoEL (1,"ernanda", "ingles",8.5,7,10)
aluno2 = AlunoEL (2,"Luiza", "espanhol",8.5,7,10)
aluno1.setNome("Fernanda")
aluno1.calcMedia()
aluno2.calcMedia()
nome1 = aluno1.getNome()
media1 = aluno1.getMedia()
nome2 = aluno2.getNome()
media2 = aluno2.getMedia()
print(nome1, "tem media igual a", media1)
print(nome2, "tem media igual a", media2)