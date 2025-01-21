<?php

$a = 10.52;
$b = pow(1.5, 4);

printf(gettype($a) . "<br>");
printf(gettype($b) . "<br>");

$c = "TransFOrmeZ unE ChaîNE écRITe dans des cASses diFFéreNTes afiN
qUe chAQue MOT ait une inITiale en MAJUSCULE";

$result = "";
$isNewWord = true;

for ($i = 0; $i < strlen($c); $i++) {
    $char = $c[$i];

    if ($char == " " || $char == "\n") {
        $result .= $char;
        $isNewWord = true;
    } else {
        if ($isNewWord) {
            $result .= strtoupper($char);
            $isNewWord = false;
        } else {
            $result .= strtolower($char);
        }
    }
}

echo $result;
echo "<br>";
echo date("l jS \\of F Y");
echo "<br>";

$age = array("Peter" => "35", "ben" => "37", "Joe" => "45");
$tab = array(
    "Dupont" => array("Paul", "Paris", 27),
    "Schmoll" => array("Kirk", "Berlin", 35),
    "Smith" => array("Stan", "Londres", 45)
);

echo $age["Peter"];
echo "<br>";
echo $tab["Smith"][1];
echo "<br>";

function ligne($x, $valeur) {
    echo "<tr><td>$x</td><td>" . number_format($valeur, 3) . "</td></tr>";
}

$sinusTable = [];
for ($x = 0; $x < 46; $x++) {
    $sinusTable[$x] = sin($x);
}

echo '<table border="1" width="50%">';
echo "<caption><b>Tableau de valeurs de sinus</b></caption>";
echo "<tr><th>X</th><th>sin(X)</th></tr>";

foreach ($sinusTable as $x => $valeur) {
    ligne($x, $valeur);
}
echo "</table>";
echo "<br>";

?>
