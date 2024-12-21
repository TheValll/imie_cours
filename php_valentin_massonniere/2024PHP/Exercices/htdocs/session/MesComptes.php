<?php
session_start(); // On démarre la session AVANT toute chose
?>
<!DOCTYPE html>
<html>
    <body>
    <h1>Fichier MesComptes.php</h1>
        <?php
        if (isset($_SESSION['id']) == false)
        {
            echo "id non defini";
            
        }
        else
        {
            echo "Compte de Mr " . $_SESSION['id'];
            $MonComptetab = array("PEL"=>"1000", "CEL"=>500);
            DrawTable($MonComptetab);
        }
        
function DrawTable($compteTab)
{
    echo '
        <table>
			<tr>
				<th></th>
				<th scope="col">Disponible</th>
			</tr>';
    foreach ($compteTab as $compteId => $compteValeur)
    {
	   echo '<tr>
				<th scope="row">' . $compteId . '</th>
				<td>' . $compteValeur . '</td>
			</tr>';
    }
	echo "</table>";

}
        
         ?>
    </body>
</html>