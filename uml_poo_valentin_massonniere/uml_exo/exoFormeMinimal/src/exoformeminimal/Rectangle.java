/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exoformeminimal;

import java.awt.Graphics;

/**
 *
 * @author droch
 */
public class Rectangle extends Forme{
    protected int largeur;
    protected int hauteur;

    public Rectangle(Point p, int largeur, int hauteur)
    {
        this.addPoint(p);
        this.largeur = largeur;
        this.hauteur = hauteur;
    }

    public String toString()
    {
        return "Je suis un rectangle, hauteur= " + this.hauteur + " largeur= " + this.largeur;
    }

    @Override
    public void draw(Graphics g) {
            Point origine = this.getPoint(0);
            g.drawRect(origine.getX(), origine.getY(), largeur, hauteur);
    } 
}
