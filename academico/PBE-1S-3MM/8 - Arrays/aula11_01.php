<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula11_01 - 30/10/25</title>
</head>
<body>
    <h1>Aula11_01 - 30/10/25 - Arrays</h1>
    <?php
    $x=10;
    $x=7.5;
    $x="teste";
    echo "x=$x<br>";
    // $y=array(10,7.5,"teste");
    // 0   1   2
    $y=[10,7.5,"teste"];
    echo "<br>y=". $y[1]; // posição do dado(Valor)
    echo "<br>";
    print_r($y);

    echo "<br> y[0] = " .$y[0]; // valor 10
    echo "<br> y[1] = " .$y[1]; // 7.5
    echo "<br> y[2] = " .$y[2]; // teste 

    echo "<hr>";

    $y[0]%=2; // 0
    $y[1]+=0.5; // 8
    $y[2].=",123"; // teste,123

    echo "<br> y[0] = " .$y[0];
    echo "<br> y[1] = " .$y[1];
    echo "<br> y[2] = " .$y[2];

    echo"<hr>";

    echo "<h3>Array associativo</h3>";

    $estudante=[
    "ra"=>1234,
    "nome"=>"Bete",
    "av1"=>8,
    "av2"=>7.5
    ];

    /*
    mostrar todos os dados do estudante e ecalcular a media entre av1 e av2
    */

    echo "<br>Estudante:" .$estudante["nome"];
    echo "<br>RA:" .$estudante["ra"];
    echo "<br>av1:" .$estudante["av1"];
    echo "<br>av2:" .$estudante["av2"];
    echo "<br> media = " . ($estudante["av1"] + $estudante ["av2"]) / 2 ;
    // ou $media= ($estudante["av1"]+$estudante["av2"])/2;

    // $_POST = array associativo;

    echo "<hr>";



    echo "<h3> Array Multidimencional</h3>";

    $num=[
    [1,2,3], // posição 0     -- ARRAY
    [4,5,6], // posição 1     -- INDEXADO
    [7,8,9] // posição 2
    ];

    echo "<br> num = " .$num[1][0];

    $naval =[
    ["água","água","submarino","água"],
    ["veleiro","água","água","água"],
    ["água","água","água","avião"],
    ["água","trem","água","água"]
    ];
    // imprimir veleiro trem submarino avião
    echo "<br>";
    echo "veleiro: " . $naval[1][0];
    echo "<br>trem: " . $naval[3][1];
    echo "<br>submarino: " . $naval[0][2];
    echo "<br>avião:" . $naval[2][3];

    

    ?>   
</body>
</html>