
<?php
session_start();

include "aula13_menu.php";

// Destruindo a sessão
session_destroy();

// Limpando os dados da variável $_SESSION
$_SESSION = array();

echo 'Sessão Finalizada.';
?>
<h2>aula13_destroy</h2>
<a href="/index.php">Página Inicial</a>