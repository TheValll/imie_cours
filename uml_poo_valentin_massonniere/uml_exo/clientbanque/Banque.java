package clientbanque;

import java.util.ArrayList;

public class Banque{
        private String name;
        private String adresse;
        private ArrayList<Compte> listComptes = new ArrayList<>();

        public Banque(String pNom, String pAdresse){
            this.name = pNom;
            this.adresse = pAdresse;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getAdresse() {
            return adresse;
        }

        public void setAdresse(String adresse) {
            this.adresse = adresse;
        }

        public ArrayList<Compte> getListComptes() {
            return listComptes;
        }

        public void setListComptes(ArrayList<Compte> listComptes) {
            this.listComptes = listComptes;
        }

        public void addAccount(Compte compte){
            this.listComptes.add(compte);
        }

        @Override
        public String toString() {
            return "Banque [name=" + name + ", adresse=" + adresse + "]";
        }

}