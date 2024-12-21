<!DOCTYPE html>
<html>
    <body>
    <h1>Fichier transfert_fichier.php</h1>
        <?php
        // Testons si le fichier a bien été envoyé et s'il n'y a pas d'erreur
         if (isset($_FILES['monfichier']) AND $_FILES['monfichier']['error'] == 0)
        {
             // Testons si le fichier n'est pas trop gros
            if ($_FILES['monfichier']['size'] <= 1000000)
            {
                // Testons si l'extension est autorisée
                //print_r($_FILES['monfichier']);
                $infosfichier = pathinfo($_FILES['monfichier']['name']);
                $extension_upload = $infosfichier['extension'];
                $extensions_autorisees = array('jpg', 'jpeg', 'gif', 'png', 'xml');
                if (in_array($extension_upload, $extensions_autorisees))
                {
                    echo "Le fichier a la bonne extension<br/>";
                    // On peut valider le fichier et le stocker définitivement
                    $result = move_uploaded_file($_FILES['monfichier']['tmp_name'], '../uploads/' . basename($_FILES['monfichier']['name']));
                    if ($result == true)
                        echo "La sauvegarde a bien été effectuée !";
                    else
                        echo "La sauvegarde a échouée";
                }
                else
                {
                    echo "Extension non attendue";
                }
            }
        }
        ?>
    </body>
</html>