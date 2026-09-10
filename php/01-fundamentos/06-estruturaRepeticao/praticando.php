<?php 
// for

    echo "Lista de Frutas:<br>";

    $frutas =["Laranja","Maça","Uva","Melância"];

    for($i=0;$i<count(($frutas));$i++){
        echo $frutas[$i]."<br>";
    }

    echo "<hr>";
    $voltas = 0;
    while($voltas<count($frutas)){
        echo "$frutas[$voltas]<br>";
        $voltas++;
    }

    echo "<hr>";
    
    foreach($frutas as $fruta){
        echo "$fruta<br>";
    }


?>
