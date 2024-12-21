package clientbanque;

import java.util.ArrayList;

public class Client {
    private String firstname;
    private String name;
    private ArrayList<Compte> listComptesClient = new ArrayList<>();

    public Client(String pFirstName, String pName){
        this.firstname = pFirstName;
        this.name = pName;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Compte> getListComptesClient() {
        return listComptesClient;
    }

    public void setListComptesClient(ArrayList<Compte> listComptesClient) {
        this.listComptesClient = listComptesClient;
    }

    public void addAccount(Compte compte){
        this.listComptesClient.add(compte);
    }

    @Override
    public String toString() {
        return "Client [firstname=" + firstname + ", name=" + name + "]";
    }
}