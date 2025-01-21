<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    function testValue($data) {
        return htmlspecialchars(trim($data));
    }

    $name = isset($_POST['name']) ? testValue($_POST['name']) : "Not send";
    $firtname = isset($_POST['firtname']) ? testValue($_POST['firtname']) : "Not send";
    $age = isset($_POST['age']) ? testValue($_POST['age']) : "Not send";

    echo "<h1>Hello, $firtname $name !</h1>";
    echo "<p>Age : $age y</p>";

    echo "<h2>Data :</h2>";
    echo "<ul>";
    foreach ($_POST as $champ => $valeur) {
        echo "<li>$champ : " . testValue($valeur) . "</li>";
    }
    echo "</ul>";
} else {
    echo "<h1>Erreur : Only post method allowed.</h1>";
}
?>
