<?php
$idade = 5;

if ($idade >=18){
    echo "Você é maior de idade\n";
}else{
    echo "Você é menor de idade\n";
}

echo"Case 2 'if Else'\n";

if ($idade>=1 && $idade<=13){
    echo"Você é uma Criança\n";

}else if( $idade>=14 && $idade<=17){
    echo"Você é adolescente\n";

}else if ($idade>=18 && $idade<=59) {
    echo "Você é Adulto\n";
    
}else if ($idade<1){
    echo "Digite um valor maior ou igual a 1!\n";
}else{ echo"Você é idoso\n";}

echo "Case 3: Ternário\n";

$limiteProduto = 5;
$qtdSelecionada = 3;

$aviso = ($qtdSelecionada>$limiteProduto) ? "A venda deste produto está limitada a no máximo 5 unidades por cliente" : "Finalizar pagamento";
    // ou qtdSelcionada = 3
    // $aviso = ($qntdSelecionada>5) ? "A venda deste produto está limitada a no máximo 5 unidades por cliente" : "Finalizar pagamento";  <-- enxuto
echo "$aviso";


?>