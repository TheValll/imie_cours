<?php

namespace App\DataFixtures;

use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;
use App\Entity\Article;
use App\Entity\Category;
use App\Entity\Comment;

class ArticlesFixtures extends Fixture
{
    public function load(ObjectManager $manager)
    {
        $categories = [
            'Technology' => 'La technologie est en constante évolution.',
            'Health' => 'La santé est essentielle pour vivre longtemps et en pleine forme.',
            'Lifestyle' => 'Adopter un style de vie sain et équilibré est crucial.'
        ];

        $categoryEntities = [];
        foreach ($categories as $title => $description) {
            $category = new Category();
            $category->setTitle($title)
                     ->setDescription($description);
            $manager->persist($category);
            $categoryEntities[] = $category; 
        }

        foreach ($categoryEntities as $category) {
            for ($j = 1; $j <= mt_rand(4, 6); $j++) {
                $article = new Article();
                $content = '<p>Voici le contenu de l\'article numéro ' . $j . ' sur ' . $category->getTitle() . '.</p>';
                $content .= '<p>Ce texte est un contenu factice utilisé pour les tests des fixtures dans Symfony.</p>';

                $article->setTitle('Article ' . $j . ' sur ' . $category->getTitle())
                        ->setContent($content)
                        ->setImage('https://via.placeholder.com/150')
                        ->setCreateAt(new \DateTime('now'))
                        ->setCategory($category);
                $manager->persist($article);

                for ($k = 1; $k <= mt_rand(4, 8); $k++) {
                    $comment = new Comment();
                    $commentContent = '<p>Ceci est un commentaire pour l\'article ' . $article->getTitle() . '.</p>';
                    $comment->setAuthor('Utilisateur ' . $k)
                            ->setContent($commentContent)
                            ->setCreatedAt(new \DateTime('now'))
                            ->setArticle($article);
                    $manager->persist($comment);
                }
            }
        }
        $manager->flush();
    }
}
