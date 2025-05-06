package appli;

import org.junit.Test;

import static org.junit.Assert.*;

public class TriangleTest {

    @Test
    public void testTriangleEquilateral() {
        Triangle triangle = new Triangle(10);
        triangle = new Triangle(5);
        assertEquals("équilatéral", triangle.getType());
    }

    @Test
    public void testTriangleIsosceles() {
        Triangle triangle = new Triangle(10);
        assertEquals("isocèle", triangle.getType());
    }

    @Test
    public void testTriangleScalene() {
        Triangle triangle = new Triangle(10);
        assertEquals("scalène", triangle.getType());
    }

    @Test
    public void testGetters() {
        Triangle triangle = new Triangle(10);
        assertTrue(triangle.getA() >= 0 && triangle.getA() <= 10);
        assertTrue(triangle.getB() >= 0 && triangle.getB() <= 10);
        assertTrue(triangle.getC() >= 0 && triangle.getC() <= 10);
    }
}