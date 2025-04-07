public function createModify(Article $article = null, Request $request, ManagerRegistry $doctrine)
    {
        if (!$article) {
            $article = new Article();
        }
        $form = $this->createForm(ArticleType::class, $article);
        
        $form->handleRequest($request);

        dump($article);
        if ($form->isSubmitted() && $form->isValid()) {
            if (!$article->getId()) {
                $article->setCreateAt(new \DateTime());
            }

            $manager = $doctrine->getManager();
            $manager->persist($article);
            $manager->flush();

            return $this->redirectToRoute('blog_show', ['id' => $article->getId()]);
        }
    }