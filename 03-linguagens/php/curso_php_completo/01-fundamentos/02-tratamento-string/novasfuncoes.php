<?php
$mensagem = "Curso completo de PHP";

# Confirmar se a string possui o valor informado -> função str_contains > retorna valor boolean (true, false)

#método longo 
$possui = str_contains($mensagem,'completo'); 
// str_contains requer dois parâmetros, 1-> onde será a pesquisa | 2-> valor a ser verificado

echo "Possui: ".$possui."\n"; // 1 = true (possui recebeu valor boolean, que em um comando echo é tratado como 0 ou 1)
echo "GETTYPE: ".gettype($possui)."\n"; // <- gettype mostra apenas o tipo, mas não o valor (true ou false)

// neste cenário, conforme a necessidade da lógica  a varíavel $possui pode ser utilizada para operações lógicas(condição, comparação).


echo 'var_dump($possui): ';
var_dump($possui);

echo "::::::::::::::::::::::::::::::::::::::::::\n";
echo 'Método curto -> var_dump aninhado com str_contains($mensagem):'. "\n";

#método curto 
var_dump(str_contains($mensagem,'completo'));
// var_dump é uma função de depuração que exibe o tipo de dado, o valor e tamanho.



# Confirmar se a string começa com valor informado -> função str_start_with > retorna valor boolean (true, false)






# Confirmar se a string termina com o valor informado -> função str_ends_with > retorna valor boolean (true, false)

