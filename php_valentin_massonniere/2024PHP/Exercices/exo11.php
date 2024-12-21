<!DOCTYPE html>
<html  >
<head>
     <meta charset="utf-8" />
     Exo12
</head>
<body>
<?php

class FabriqueFormulaire 
{
    private $titreFormulaire;
    private $actionFile;
    private $controlList=array();

    public function __construct($titreFormulaire, $actionFile)
    {
        $this->titreFormulaire = $titreFormulaire;
        $this->actionFile = $actionFile;
    }

    public function AddControl($type, $label, $name, $value)
    {
        switch  ($type)
        {
            case "text":
            case "submit":
                $newCtrl = new Control($type, $label, $name, $value);
            break;
            //case "submit":
            //    $newCtrl = new Control($type, $label, $name, $value);
            //break;
            case "list":
                $newCtrl = new CtrlList($type, $label, $name, $value);
            break;
            default :
                //throw new Exception("Controle $type pas encore implémenté");
                break;
        }
        $this->controlList[] = $newCtrl;
        return $newCtrl;
    }

    public function Afficher()
    {   // Afficher le formulaire complet
        echo "		<form action=\"$this->actionFile\" method=\"post\">
        <fieldset>
            <legend>$this->titreFormulaire</legend>
            <table border=\"0\" >
            ";
        foreach ($this->controlList as $control)
        {
            $control->Afficher();
        }
        echo "			</table>
        </fieldset>
	</form>";
    }
    public function LoadFromFile(string $fileName)
    {
        if(is_file($fileName))
        {
            $xml = simplexml_load_file($fileName);
            foreach ($xml->children() as $inputEntity) {
                $this->AddControl($inputEntity['type']->__toString(), $inputEntity['label']->__toString(), $inputEntity['name']->__toString(), $inputEntity['value']->__toString());
            }
        }
    }

}

class Control{
    // controle de formulaire
    protected $type;
    protected $label;
    protected $name;
    protected $value;

    public function __construct($type, $label, $name, $value)
    {
        $this->type = $type;
        $this->label = $label;
        $this->name = $name;
        $this->value = $value;
    }
    public function Afficher()
    {
        echo "<tr>
        <td>$this->label</td>
        <td><input type=\"$this->type\" name=\"$this->name\" value=\"$this->value\"></td>
    </tr>";
    }

}

/*class CtrlText extends Control {
    public function Afficher()
    {
        echo "<tr>
        <td>$this->label</td>
        <td><input type=\"text\" name=\"$this->name\" value=\"$this->value\"></td>
    </tr>";
    }
   
}
class CtrlSubmit extends Control {
    public function Afficher()
    {
        echo "<tr>
        <td>$this->label</td>
        <td><input type=\"submit\" name=\"$this->name\" value=\"$this->value\"></td>
    </tr>";
    }
   
}*/

class CtrlList extends Control {
    private $tabOption = array();
    public function AddOption(string $optionValue, string $optionText)
    {
        $this->tabOption[] = array($optionValue, $optionText);
    }
    public function Afficher()
    {
        echo "<tr>
        <td>$this->label</td>
        <td>
        <select name=\"$this->name\">";
        foreach ($this->tabOption as $option)
        {
            echo "<option value=\"" . $option[0] . "\">" . $option[1] . "</option>";
        }
        /*    <option value=\"france\">France</option>
            <option value=\"belgique\">Belgique</option>
            <option value=\"canada\">Canada</option>*/
        echo "  </select>
        </td>
    </tr>";
    }
   
}



$formulaire = new FabriqueFormulaire("Titre de mon formulaire", "toto.php");

$formulaire->AddControl("text","Votre nom","cc","dd" );
$formulaire->AddControl("submit","AA","ZZ","WW" );
$ctrlList = $formulaire->AddControl("list","AAqq","ZZdd","WWdd" );
$ctrlList->AddOption("france", "France");
$ctrlList->AddOption("canada", "Canada");
$formulaire->Afficher();

$autreformulaire = new FabriqueFormulaire("Formulaire depuis fichier xml", "toto.php");
$autreformulaire->LoadFromFile("./form.xml");
$autreformulaire->Afficher();

/*$file = "./form.xml";
$xml = simplexml_load_file($file);
$tabXml = array();
foreach ($xml->children() as $inputEntity) {
    $tabXml[] = array($inputEntity['type']->__toString(), $inputEntity['label']->__toString(), $inputEntity['name']->__toString(), $inputEntity['value']->__toString());
}
*/
/* $tab = array();
$text = new CtrlText("aa","bb","cc","dd");
$tab[] = $text;
//$tab = array();

foreach ($tab as $ctrl)
{
    $ctrl->Afficher();
}

$file = "./formulaires.xml";
if(is_file($file))
{
    $xml=simplexml_load_file($file) or die("Error: Cannot create object");\\
    $form = $xml[0];
    $aa=$form[0];
    echo " ";
}


print_r($xml);*/
?>
</body>
</html>