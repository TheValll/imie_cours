package exoformeminimal;

public class Carre extends Rectangle{
    protected int cote;

    public Carre(Point p, int cote) {
        super(p, cote, cote);
        this.cote = cote;
    }
}
