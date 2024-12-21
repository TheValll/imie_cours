package exoformeminimal;


import java.awt.*;

public class Segment extends Forme{

    private Point p1;
    private Point p2;

    public Segment(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
        this.addPoint(p1);
        this.addPoint(p2);
    }

    public void draw(Graphics g) {
        Point origine = this.p1;
        Point finish = this.p2;
        g.drawLine(origine.getX(), origine.getY(), finish.getX(), finish.getY());
    }
}
