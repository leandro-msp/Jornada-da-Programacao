<?php
//VARIÁVEL  
$nota = 10.0;
$idade= 26;
$nome="Leandro";

echo "Meu nome é $nome, tenho $idade anos, e obtive nota $nota.\n";

echo'Tipo da variável $nome e seu valor: ';
var_dump($nome);

//CONSTANTE 
define("USUARIO","admin");

echo USUARIO;
?>