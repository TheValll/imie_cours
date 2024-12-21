package exoformeminimal;

import java.awt.Graphics;

public class ArcEllipse extends Forme{
	
	protected int a;
	private int b;
	protected int angle1;
	protected int angle2;
	
	public ArcEllipse(Point p, int a, int b, int angle1, int angle2)
	{
		this.a = a;
		this.b = b;
		this.angle1 = angle1;
		this.angle2 = angle2;
		super.addPoint(p);
	}
	
	public String toString()
	{
		return "Je suis un arc d'ellipse, rayon1= " + this.a + " rayon2= " + this.b + " angle1= " + this.angle1 + " angle2= " + this.angle2;
	}

	@Override
	public void draw(Graphics g) {
		Point origine = this.getPoint(0);
		// drawArc(x,y,width, height, startangle, arcAngle)
		// l'arc est contenu dans le rectangle (x,y,width, height)
		// il faut calculer le point haut gauche du rectangle connaissant le centre de l'arc
		int x = origine.getX() - (int)((float)a/2.0);
		int y = origine.getY() - (int)((float)b/2.0);
		//g.drawArc(origine.getX(), origine.getY(), a, b,angle1, angle2 - angle1);
		g.drawArc(x, y, a, b,angle1, angle2 - angle1);
		
	}

}

