<?php
class Article {
    private $id;
    private $name;
    private $brand;
    private $price;

    public function __construct($id, $name, $brand, $price) {
        $this->id = $id;
        $this->name = $name;
        $this->brand = $brand;
        $this->price = $price;
    }

    public function display() {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($this->id) . "</td>";
        echo "<td>" . htmlspecialchars($this->name) . "</td>";
        echo "<td>" . htmlspecialchars($this->brand) . "</td>";
        echo "<td>" . number_format($this->price, 2) . " €</td>";
        echo "</tr>";
    }
}

class Articles {
    private $articles = [];

    public function fetchArticlesFromDB($database) {
        $query = $database->query('SELECT * FROM articles');
        $results = $query->fetchAll(PDO::FETCH_ASSOC);

        foreach ($results as $row) {
            $this->articles[] = new Article($row['id'], $row['nom'], $row['marque'], $row['prix']);
        }
    }

    public function display() {
        echo '<table border="1" width="50%">';
        echo '<caption><b>List of articles</b></caption>';
        echo '<tr><th>ID</th><th>Name</th><th>Brand</th><th>Price</th></tr>';

        foreach ($this->articles as $article) {
            $article->display();
        }

        echo '</table>';
    }
}
?>
