<?php
use PHPUnit\Framework\TestCase;
/*
Pour mettre en place PHPUnit :
- vérifier que composer existe par composer -V  sinon l'installer
- installer PHPUnit localement au projet par la commande : composer require --dev phpunit/phpunit
- Arrêter et relancer Visual Studio Code
- créer un dossier test
- dans le dossier test créer des fichiers dont le nom se terminent par Test.php
- Dans un fichier test :
    - le nom de la classe doit être identique au nom de fichier. La classe hérite de TestCase
    - créer une méthode par test. Chaque méthode contient un assert  : $this->assertXXX()
- lancer les tests dans une fenêtre console par : ./vendor/bin/phpunit test 
*/

class PersonPHPUnitTest extends TestCase
{
    public function testBidon()
    {
        $this->assertTrue(1 == 1, "Ioustone, On a un probleme !");
    }
}