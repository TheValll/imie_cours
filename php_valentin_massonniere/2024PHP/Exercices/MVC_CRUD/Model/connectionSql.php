

<?php class Database { 
    private static $dbName = 'PersonFilm' ; 
    private static $dbHost = 'localhost' ; 
    private static $dbUsername = 'root'; 
    private static $dbUserPassword = ''; 
    private static $cont = null; 
    public function __construct() { 
        die('Init function is not allowed'); 
    } 
    public static function connect() { 
        // Connexion à la base de données

        if ( null == self::$cont ) 
        { 
        try 
            { 
                self::$cont = new PDO( "mysql:host=".self::$dbHost.";"."dbname=".self::$dbName, self::$dbUsername, self::$dbUserPassword); 
            } 
        catch(PDOException $e) 
        { 
            die($e->getMessage()); 
        }
       }
       //print_r(self::$cont);
       return self::$cont;
    }
     
    public static function disconnect()
    {
        self::$cont = null;
    }
}
?>
