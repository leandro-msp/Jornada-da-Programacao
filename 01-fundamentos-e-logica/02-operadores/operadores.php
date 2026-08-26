<?php
//ARITIMÉTICOS

$a = 20;
$b = 4;

$soma = $a+$b;
$subtracao =  $a-$b;
$multiplicacao = $a*$b;
$divisao = $a/$b;
$resto = $a%$b; // ou também chamado de módulo
$exponencial = $a**$b;
                                                    // Operação direto no comando de saída:
echo "Soma: $soma\n";                               // echo "Soma: ". ($a+$b)."\n";
echo "Subtração: $subtracao\n";                     // echo "Subtração: ".($a-$b)."\n";
echo "Mutiplicação: $multiplicacao\n";              // echo "Multiplicação: ".($a*$b)."\n";
echo "Divisão: $divisao\n";                         // echo "Divisão: ".($a/$b)."\n";
echo "Resto da Divisão: $resto\n";                  // echo "Resto da Divisão: ".($a%$b)."\n";
echo "Exponencial: $exponencial\n";                 // echo "Exponencial(^): ".($a**$b)."\n";

//ATRIBUIÇÃO
$a = 10;
$b = 5;

echo "a = $a \n";
echo "b = $b \n";

$a+=10; // soma o valor atual da variável + 10
// $a = $a+10 | 10+10 | a = 20
echo "Novo valor de 'a' = $a \n";
$b*=5; // $b = $b * 5 | 5*5 | b = 25
echo "Novo valor de 'b' = $b \n";

$b-=$a; // $b = $b - $a || 20 - 25 || $b = 25 - 20 | $b = 5

echo "Novo valor de 'b': $b \n";

$c = $b-=($b*2); //$c = $b - ($b/2) || $c = 5 -(10) | $c = 5 - 10 || %c = -5
echo "c = $c\n";

$d = 8;
$c+=$d;
echo "Novo valor de 'c'= $c \n";
$d%=$c; // $d = $d%$c || $d = 8%3 | $d = 2
echo "d = $d \n";


//COMPARAÇÃO
    # Operadores de Comparação retorna valores Booleanos (Falso(0) ou Verdadeiro(1)).


$e=100;
$f= "100";

$igual = $e==$f;
echo "E e F São iguais: $igual \n";

$identico = $e===$f;
echo "E e F são idênticos: $identico \n"; 
// var_dump($identico);

// $identico = (int)$identico;
// echo "Valor de identico : $identico\n";

$naoIgual = $e!=$f;
echo "E e F não são iguais: $naoIgual\n";

$naoIdentico = $e!==$f;
echo "E e F não são idênticos: $naoIdentico \n";

$diferente = $e<>$f;
echo "E e F são diferentes: $diferente \n";


$g = 20;
$h = 30;
$i = 40;
$j = 20;

$menor = $g<$h;
echo "G é menor que H: $menor \n";

$maior = $h>$i;
echo "H é maior que I: $maior\n";

$menorIgual = $g<=$i;
echo "G é igual ou Menor a I: $menorIgual \n";

$maiorIgual = $j>=$g;
echo"J é maior ou Igual a G: $maiorIgual\n";

// $teste1 = "a";
// $teste2 = "b";

// $final = $teste1 > $teste2;
// echo "final: $final";

//LÓGICOS

$idade1 = 25;
$idade2 = 18;
$idade3 = 30;
$idade4 = 30;

$a1 =  $idade1 < $idade2;
$a2 = !($idade1 < $idade2);


echo"a1 = \n";
    var_dump($a1);

echo"a2 = \n";
    var_dump($a2);


$c = "String";
$d = "String";

$e1 = !($c!=$d);

echo "e1:\n";
    var_dump($e1);


$e2 = !($c!=$d);
echo "e2:\n";
    var_dump($e2);


$e3 = !($idade3===$idade4);
echo "e3:\n";
    var_dump($e3);


# AND | &&

$f1 = (($idade1>$idade2) and ($idade3>=$idade4));
echo "f1: \n";
    var_dump($f1);

$f2 = (($idade3!=$idade1) && !($idade2<$idade1));
    // Operador E |and | && --> o que mais se aplica em cenários de autenticação, exemplo de login:
    // O sistema faz a leitura do banco de dados, e chega se ambas informações coincidem.
echo "f2:\n";
    var_dump($f2);

# Or , ||

$g = (($c!=$d) or !($idade2>=$idade4));
$h = !(($c!=$d) || ($d==="string"));

echo "g:\n";
    var_dump($g);

echo "h:\n";
    var_dump($h);


#XOR -> OU exclusivo

$a = "10";
$b = 10;
$c = ($b+(int)$a);


$d1 = (($b==$a) xor ($c<$b));
$d2 = ((($c/2)==10) xor (($b%2)==0));
echo "d1:\n";
    var_dump($d1);

echo "d2:\n";
    var_dump($d2);

#OPERADOR TERNÁRIO

$temperatura=15;

$checagem = ($temperatura <=17) ? "Está Frio" : "Está Calor";

echo "$checagem";

?>