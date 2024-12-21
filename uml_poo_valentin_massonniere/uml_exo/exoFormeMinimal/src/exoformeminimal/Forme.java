package exoformeminimal;

import java.awt.Graphics;
import java.util.ArrayList;

public abstract class  Forme {
	private ArrayList<Point> pointList = new  ArrayList<Point>();
	
	public void addPoint(Point p)
	{
		pointList.add(p);
	}
	
	public Point getPoint(int rang)
	{
		if (rang >= 0 && rang < pointList.size())
			return pointList.get(rang);
		return null;
	}
	public abstract void draw(Graphics g);

}
