<?php

namespace App\Entity;

use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Security\Core\User\UserInterface;

/**
 * @ORM\Entity(repositoryClass="App\Repository\UserRepository")
 * @ORM\Table(name="users")
 */
class User implements UserInterface
{
    /**
     * @ORM\Id()
     * @ORM\GeneratedValue(strategy="AUTO")
     * @ORM\Column(type="integer")
     */
    private int $id;

    /**
     * @ORM\Column(type="string", length=180, unique=true)
     */
    private string $email;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private string $username;

    /**
     * @ORM\Column(type="string")
     */
    private string $password;

    /**
     * @ORM\Column(type="boolean")
     */
    private bool $isActive;

    /**
     * @ORM\Column(type="json")
     */
    private array $roles = [];

    /**
     * @param string $email
     * @param string $username
     * @param string $password
     * @param array $roles
     */
    public function __construct(string $email, string $username, string $password, array $roles = [])
    {
        $this->email = $email;
        $this->username = $username;
        $this->password = $password;
        $this->roles = $roles;
        $this->isActive = true; // Par défaut, l'utilisateur est actif
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getEmail(): string
    {
        return $this->email;
    }

    public function setEmail(string $email): self
    {
        $this->email = $email;
        return $this;
    }

    public function getUsername(): string
    {
        return $this->username;
    }

    public function setUsername(string $username): self
    {
        $this->username = $username;
        return $this;
    }

    public function getPassword(): string
    {
        return $this->password;
    }

    public function setPassword(string $password): self
    {
        $this->password = $password;
        return $this;
    }

    public function getRoles(): array
    {
        return array_merge($this->roles, ['ROLE_USER']);
    }

    public function setRoles(array $roles): self
    {
        $this->roles = $roles;
        return $this;
    }

    /**
     * Cette méthode est utilisée pour identifier l'utilisateur.
     * @return string
     */
    public function getUserIdentifier(): string
    {
        return $this->email; // Vous pouvez aussi utiliser username ou un autre champ unique.
    }

    public function eraseCredentials()
    {
        // Effacer les mots de passe en cache après l'authentification
        $this->password = null; // On efface le mot de passe de la mémoire.
    }

    public function isActive(): bool
    {
        return $this->isActive;
    }

    public function setActive(bool $isActive): self
    {
        $this->isActive = $isActive;
        return $this;
    }
}
