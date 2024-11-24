package clientbanque;

public class Compte{
    private String nom;
    private int valeur;
    private Client client;
    private Banque banque;
    
    public Compte(String nom, int valeur, Client client, Banque banque) {
        this.nom = nom;
        this.valeur = valeur;
        this.client = client;
        this.banque = banque;
        this.banque.addAccount(this);
        this.client.addAccount(this);
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getValeur() {
        return valeur;
    }

    public void setValeur(int valeur) {
        this.valeur = valeur;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

    public Banque getBanque() {
        return banque;
    }

    public void setBanque(Banque banque) {
        this.banque = banque;
    }

    @Override
    public String toString() {
        return "Compte [nom=" + nom + ", valeur=" + valeur + ", client=" + client + ", banque=" + banque + "]";
    }  
    
}
