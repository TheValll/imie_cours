package exoformeminimal;

public class Cercle extends ArcEllipse{

    protected int rayon;

    public Cercle(Point p, int rayon) {
        super(p, rayon, rayon, 0, 360);
        this.rayon = rayon;
    }
}
