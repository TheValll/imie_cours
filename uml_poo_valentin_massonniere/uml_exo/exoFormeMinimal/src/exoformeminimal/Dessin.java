package exoformeminimal;

import java.awt.*;
import java.util.ArrayList;
import java.util.Vector;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

// Cette classe herite de canvas pour redefinir la
// methode paint. La vue est codee dans cette classe
class Dessin extends Canvas {
	/**
	 * 
	 */
	
	private ArrayList<Forme> listForm = new ArrayList<Forme>();
		
	Color couleur ;
	
	// le constructeur de la classe
	public Dessin() {
            couleur = Color.blue ;
            this.setBackground(Color.white);
	}
        
        @Override
	public void paint(Graphics g) {
            // un rectangle noir encadre le composant
            g.setColor(Color.black);
            g.drawRect(0, 0, this.getWidth() - 1, this.getHeight() - 1);
            //le texte est affiche
            //g.drawString(text, 10, 15);
            //la couleur est choisie
            g.setColor(couleur);

            for (Forme form : listForm)
            {
                    form.draw(g); // on demande à toutes les formes de la liste de se tracer
            }
	}
	
	// ajout d'une forme dans le dessin
	public void addForme(Forme forme)
	{
            listForm.add(forme);
	}
	
	//La redefinition de cette methode permet de specifier
	//la taille preferee du composant
	public Dimension getPreferredSize() {
            return new Dimension(400, 400);
	}
}
