package appli;

import java.util.Random;

public class Triangle {

    private float a;
    private float b;
    private float c;

    public Triangle(float max) {
        Random rand = new Random();
        this.a = rand.nextFloat() * max;
        this.b = rand.nextFloat() * max;
        this.c = rand.nextFloat() * max;
    }

    public String getType() {
        if (a == b && b == c) {
            return "équilatéral";
        } else if (a == b || b == c || a == c) {
            return "isocèle";
        } else {
            return "scalène";
        }
    }
    public float getA() {
        return a;
    }

    public float getB() {
        return b;
    }

    public float getC() {
        return c;
    }
}
