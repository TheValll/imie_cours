<?php
session_start(); // On démarre la session AVANT toute chose
?>
<!DOCTYPE html>
<html>
    <body>
    <h1>Fichier AcceptLogin.php</h1>
        <?php
        
        if (isset($_POST['id']) == false)
        {
            echo "nom non defini";
            exit();
        }
        else if (isset($_POST['pswd']) == false)
        {
            echo "password non defini";
            exit();
        }
        else
        {
            echo "<br/>nom " . $_POST['id'];
            echo "<br/>pswd " . $_POST['pswd'];
        
            $id = htmlspecialchars($_POST['id']);
            $pswd = htmlspecialchars($_POST['pswd']);
            if ($id == "azer" && $pswd == "qsdf")
            {
                echo "<br/>Login réussi";
                $_SESSION['id'] = $id;
                $_SESSION['pswd'] = $pswd;
                echo '<br/><a href="MesComptes.php">Acces a mon compte</a>';
            }
            else
                echo "<br/>Nom ou mot de passe incorrect";
        }
        ?>
    </body>
</html>