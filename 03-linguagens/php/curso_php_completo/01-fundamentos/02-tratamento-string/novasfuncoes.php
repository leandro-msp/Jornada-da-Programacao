<?php
$mensagem = "Curso completo de PHP";

# Confirmar se a string possui o valor informado -> função str_contains > retorna valor boolean (true, false)

$possui = str_contains($mensagem,'completo');  // str_contains requer dois parâmetros: onde será a pesquisa e o valor a ser verificado
echo "Possui: ".$possui."\n"; // 1(boolean) = true 
echo "GETTYPE: ".gettype($possui)."\n"; // gettype mostra apenas o tipo, mas não o valor (true ou false)
// neste cenário, conforme a necessidade do sistema a variável $possui pode ser utilizada para operações lógicas(condição, comparação).

var_dump($possui); // var_dump é uma função de depuração que exibe o tipo de dado, o valor e tamanho.

//método curto 
echo "Str Contains: ";
var_dump(str_contains($mensagem,'completo'));  // função case_sensitive

# Confirmar se a string começa com valor informado -> função str_start_with > retorna valor boolean (true, false)
echo "Start With: ";
var_dump(str_starts_with($mensagem,'Curso')); // verifica se a string começa com o valor informado -> função case_sensitive


# Confirmar se a string termina com o valor informado -> função str_ends_with > retorna valor boolean (true, false)
echo "Ends With: ";
var_dump(str_ends_with($mensagem,'PHP')); // verfica se a string termina com o valor informado -> função case_sensitive

#método com formatação no var_dump para não cair no case sensitive

// ex.:
echo "Ends With -> php minúsculo: ";
var_dump(str_ends_with(strtolower($mensagem),'php'));