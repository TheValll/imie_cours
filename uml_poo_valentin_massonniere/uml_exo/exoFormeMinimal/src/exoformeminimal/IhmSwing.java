/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exoformeminimal;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.border.Border;

/**
 *
 * @author droch
 */
public class IhmSwing extends JFrame{
	protected Dessin dessin;
	
	public Dessin getDessin()
	{
		return dessin;
	}
	
	public IhmSwing() {
		super("Un exemple de fenetre");
		//le programme doit se terminer quand la fenetre est fermee
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// remplissage du panel principal
		JPanel mainPanel = (JPanel) this.getContentPane();
		dessin = new Dessin();
		mainPanel.add(dessin);
		// une bordure permet d’aerer l’affichage
		mainPanel.setBorder(new EmptyBorder(10, 10, 10, 10));
		// calcul de la dimension de la fenetre
		this.pack();

	}

}
