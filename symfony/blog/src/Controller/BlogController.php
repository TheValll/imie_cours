<?php

namespace App\Controller;

use App\Entity\Article;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Repository\ArticleRepository;
use Symfony\Component\HttpFoundation\Request;
use Doctrine\Persistence\ObjectManager;

final class BlogController extends AbstractController
{
    #[Route('/blog', name: 'app_blog')]
    public function index(ArticleRepository $repo): Response
    {
        // $repo = $doctrine->getRepository(Article::class);
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

    #[Route('/blog/new', name: 'blog_create')]
    public function create(Request $request, ManagerRegistry $doctrine
    )
    {
    dump($request);
    if ($request->request->count() > 0 )
    { // retour de formulaire
    $article = new Article();
    $article->setTitle($request->request->get('title'))
    ->setContent($request->request->get('content'))
    ->setImage($request->request->get('image'))
    ->setCreateAt(new \DateTime());
    $manager = $doctrine->getManager();
    $manager->persist($article);
    $manager->flush();
    return $this->redirectToRoute('blog_show', ['id' => $article-> getId()]);
    }
    return $this->render('blog/create.html.twig');
    }

    #[Route('/blog/{id}', name: 'blog_show')]
    public function show(ArticleRepository $repo, $id)
    {
    // $repo = $doctrine->getRepository(Article::class);
    $article = $repo->find($id);
    return $this->render('blog/show.html.twig',[
    'article' => $article
    ]);
    }

}
