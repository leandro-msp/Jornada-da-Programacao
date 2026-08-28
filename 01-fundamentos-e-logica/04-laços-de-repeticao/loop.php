<?php
//while / enquanto

$i = 0;
while ($i<10){ // enquanto a condição for verdadeira, a instrução será executada
    echo "$i";
    $i++;
}

//ciclo infitino

$i = 5;
while($i>0){
    echo "$i";
    $i--;
    if ($i==0){ 
        $i=5; // redefine o valor de "i" para 5, e a condição do while torna a ser verdadeira;
    }       
}

$começar = 10;
while($começar>0){
    echo "$começar";
    $começar--;    
}
echo "START!";

//pares

$num = 0;
while ($num<10){
    echo"$num";
    $num +=2; // incrementar de 2 em 2
}


//do-while

$x=5;
do{
    echo "$x";
    $x--;
}while ($x>0)

/*a Diferença entre o while e o do-while é o momento que a condição é testada
o while primeiro verifica a condição, se for verdadeira, a instrução é executada, até que torne falsa
já o do-while executa pelo menos uma vez a instrução e depois verifica a condição, mesmo que ela seja falsa desde o início
 */
?>