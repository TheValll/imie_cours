package clientbanque;

public class ClientBanque{
    public static void main(String[] args){
        Banque b1 = new Banque("CL", "70 rue Anatole France");
        Banque b2 = new Banque("BNP", "70 rue Anatole France");

        Client c1 = new Client("Valentin", "Massonniere");
        Client c2 = new Client("Sophie", "Maison");

        Compte cc1 = new Compte("Compte courant", 12000, c1, b2);
        Compte cc2 = new Compte("Compte courant", 5677, c2, b2);
        Compte cc3 = new Compte("Compte Livret A", 6788, c1, b2);

        System.out.println("Banques :");
        System.out.println(b1.toString());
        System.out.println(b2.toString());

        System.out.println("-----------");

        System.out.println("Clients :");
        System.out.println(c1.toString());
        System.out.println(c2.toString());

        System.out.println("-----------");

        System.out.println("Comptes :");
        System.out.println(cc1.toString());
        System.out.println(cc2.toString());
        System.out.println(cc3.toString());

        System.out.println("-----------");

        System.out.println("Liste comptes :");
        System.out.println(b1.getListComptes());
        System.out.println(b2.getListComptes());

        System.out.println("-----------");

        System.out.println("Liste comptes clients :");
        System.out.println(c1.getListComptesClient());
        System.out.println(c2.getListComptesClient());
    }
}
