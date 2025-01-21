<?php
try {
    $bdd = new PDO('mysql:host=localhost;dbname=PHPtest;charset=utf8', 'root', '');
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    die('<h1>Error : </h1>' . $e->getMessage());
}

try {
    $requete = $bdd->query('SELECT * FROM articles');
    $articles = $requete->fetchAll(PDO::FETCH_ASSOC);

    echo '<table border="1" width="50%">';
    echo '<caption><b>List of articles</b></caption>';
    echo '<tr><th>ID</th><th>Name</th><th>Brand</th><th>Price</th></tr>';
    foreach ($articles as $article) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($article['id']) . '</td>';
        echo '<td>' . htmlspecialchars($article['nom']) . '</td>';
        echo '<td>' . htmlspecialchars($article['marque']) . '</td>';
        echo '<td>' . number_format($article['prix'], 2) . ' €</td>';
        echo '</tr>';
    }
    echo '</table>';
} catch (Exception $e) {
    echo '<h1>Error with the data reception : </h1>' . $e->getMessage();
}
?>
