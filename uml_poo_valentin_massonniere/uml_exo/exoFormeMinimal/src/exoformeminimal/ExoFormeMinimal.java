/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exoformeminimal;

/**
 *
 * @author droch
 */
public class ExoFormeMinimal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        IhmSwing myIhm = new IhmSwing();
        Dessin dessin1 = myIhm.getDessin();
        Forme arcE = new ArcEllipse(new Point(50,50), 100,80,0,180);
	dessin1.addForme(arcE);
        
        Forme E1 = new Rectangle(new Point(100,100), 100,80);
        dessin1.addForme(E1);

        Forme C1 = new Carre(new Point(150,150), 200);
        dessin1.addForme(C1);

        Forme Cl1 = new Cercle(new Point(200, 200), 40);
        dessin1.addForme(Cl1);

        Forme E2 = new Ellispe(new Point(250, 250), 60, 120);
        dessin1.addForme(E2);

        Forme S1 = new Segment(new Point(300, 300), new Point(300, 450));
        dessin1.addForme(S1);

        Forme Cl2 = new Cercle(new Point(500, 250), 50);
        dessin1.addForme(Cl2);

        Forme S2 = new Segment(new Point(500, 275), new Point(500, 400));
        dessin1.addForme(S2);

        Forme S3 = new Segment(new Point(500, 350), new Point(450, 300));
        dessin1.addForme(S3);

        Forme S4 = new Segment(new Point(500, 350), new Point(550, 300));
        dessin1.addForme(S4);

        Forme S5 = new Segment(new Point(500, 400), new Point(450, 450));
        dessin1.addForme(S5);

        Forme S6 = new Segment(new Point(500, 400), new Point(550, 450));
        dessin1.addForme(S6);

        Forme Cl3 = new Cercle(new Point(490, 250), 10);
        dessin1.addForme(Cl3);

        Forme Cl4 = new Cercle(new Point(510, 250), 10);
        dessin1.addForme(Cl4);

        Forme S7 = new Segment(new Point(495, 250), new Point(505, 250));
        dessin1.addForme(S7);

        Forme Cl5 = new Cercle(new Point(450, 200), 100);
        dessin1.addForme(Cl5);

        myIhm.setVisible(true);

    }
    
}
