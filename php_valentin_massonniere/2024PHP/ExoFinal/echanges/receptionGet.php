<?php
if (isset($_GET['name']) && isset($_GET['firstname'])) {
    $name = htmlspecialchars($_GET['name']);
    $firstname = htmlspecialchars($_GET['firstname']);

    echo "<h1>Hello, $firstname $name !</h1>";
} else {
    echo "<h1>No data found </h1>";
}

echo "<p>Method use : " . htmlspecialchars($_SERVER['REQUEST_METHOD']) . "</p>";
?>
