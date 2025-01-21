<?php
if (isset($_FILES['myfile']) && $_FILES['myfile']['error'] === UPLOAD_ERR_OK) {
    $fileName = $_FILES['myfile']['name'];
    $fileType = $_FILES['myfile']['type'];
    $fileSize = $_FILES['myfile']['size'];
    $fileTmp = $_FILES['myfile']['tmp_name'];
    $filePath = 'uploads/';
    if (!is_dir($filePath)) {
        mkdir($filePath, 0777, true);
    }

    $finalPath = $filePath . basename($fileName);
    if (move_uploaded_file($fileTmp, $finalPath)) {
        echo "<h1>Fichier envoyé avec succès !</h1>";
        echo "<p>Name : $fileName</p>";
        echo "<p>Type : $fileType</p>";
        echo "<p>Size : " . round($fileSize / 1024, 2) . " Ko</p>";
        echo "<p>Path : $    $finalPath = $filePath . basename($fileName);
</p>";
    } else {
        echo "<h1>Error.</h1>";
    }
} else {
    echo "<h1>Error : No file send.</h1>";
}
?>
