<?php

namespace App\Controller;

use App\Entity\Article;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

final class BlogController extends AbstractController
{
    #[Route('/blog', name: 'app_blog')]
    public function index(ManagerRegistry $doctrine): Response
    {
        $repo = $doctrine->getRepository(Article::class);
        $articles = $repo->findAll();
        return $this->render('blog/index.html.twig', [
            'controller_name' => 'BlogController',
            'articles' => $articles
        ]);
    }

    #[Route('/', name: 'home')]
    public function home(): Response
    {
        return $this->render('blog/home.html.twig', [
            'title' => "Utilisation d'une variable",
            'age' => 27
        ]);
    }

    #[Route('/blog/{id}', name: 'blog_show')]
    public function show(ManagerRegistry $doctrine, $id)
    {
    $repo = $doctrine->getRepository(Article::class);
    $article = $repo->find($id);
    return $this->render('blog/show.html.twig',[
    'article' => $article
    ]);
    }
}
