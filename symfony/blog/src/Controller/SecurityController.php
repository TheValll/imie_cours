<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\HttpFoundation\Request;
use App\Entity\User;
use App\Form\RegistrationType;
use Doctrine\Persistence\ManagerRegistry;

class SecurityController extends AbstractController
{
    #[Route('/inscription', name: 'inscription')]
    public function registration(Request $request, ManagerRegistry $doctrine)
    {
        $manager = $doctrine->getManager();

        $user = new User();

        $form = $this->createForm(RegistrationType::class, $user);

        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $manager->persist($user);
            $manager->flush();

            return $this->redirectToRoute('inscription');  
        }

        return $this->render('security/registration.html.twig', [
            'form' => $form->createView(),
        ]);
    }

    #[Route('/connection', name: 'security_login')]
    public function login()
    {
        return $this->render('security/login.html.twig');
    }
}
