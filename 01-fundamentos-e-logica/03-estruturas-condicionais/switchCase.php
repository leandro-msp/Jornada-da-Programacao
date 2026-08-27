<?php
$semestre = 3;

switch($semestre){
    case 1:
        echo "Faltam 4 semestres para finalizar o curso. \n";
        break;
    case 2:
        echo "Faltam 3 semestres para finalizar o curso. \n";
        break;
    case 3:
        echo "Faltam 2 semestres para finalizar o curso. \n";
        break;
    case 4:
        echo "Falta 1 semestre para finalizar o curso. \n";
        break;
    case 5: 
        echo "Este é seu último semestre.\n";
        break;
    default:
        echo "Você ainda não iniciou o curso.\n";
}




?>