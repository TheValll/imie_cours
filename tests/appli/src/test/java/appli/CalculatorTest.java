package appli;

import org.junit.Test;

import static org.junit.Assert.*;
public class CalculatorTest {

    @Test
    public void multiplyABpositif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = 2;
        int result = a*b;

        if (calc.multiply(a, b) == result) {
            System.out.println("a and b positif");
        }
    }

    @Test
    public void multiplyApositifBnegitif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = -2;
        int result = a*b;
        if (calc.multiply(a, b) == result) {
            System.out.println("a positif and b negitif");
        }
    }

    @Test
    public void multiplyABnegitif() {
        Calculator calc = new Calculator();
        int a = -1;
        int b = -2;
        int result = a*b;
        if (calc.multiply(a, b) == result) {
            System.out.println("a and b negitif");
        }
    }

    @Test
    public void divideABpositif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = 2;
        int result = a/b;

        if (calc.divide(a, b) == result) {
            System.out.println("a and b positif");
        }
    }

    @Test
    public void divideApositifBnegitif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = -2;
        int result = a/b;
        if (calc.divide(a, b) == result) {
            System.out.println("a positif and b negitif");
        }
    }

    @Test
    public void divideABnegitif() {
        Calculator calc = new Calculator();
        int a = -1;
        int b = -2;
        int result = a/b;
        if (calc.divide(a, b) == result) {
            System.out.println("a and b negitif");
        }
    }

    @Test
    public void addABpositif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = 2;
        int result = a + b;

        if (calc.add(a, b) == result) {
            System.out.println("a and b positif");
        }
    }

    @Test
    public void addApositifBNegatif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = -2;
        int result = a + b;

        if (calc.add(a, b) == result) {
            System.out.println("a positif and b negatif");
        }
    }

    @Test
    public void addABNegatif() {
        Calculator calc = new Calculator();
        int a = -1;
        int b = -2;
        int result = a + b;

        if (calc.add(a, b) == result) {
            System.out.println("a and b negatif");
        }
    }


    @Test
    public void substractABpositif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = 2;
        int result = a - b;

        if (calc.substract(a, b) == result) {
            System.out.println("a and b positif");
        }
    }

    @Test
    public void substractApositifBnegatif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = -2;
        int result = a - b;

        if (calc.substract(a, b) == result) {
            System.out.println("a and b negatif");
        }
    }

    @Test
    public void substractABNegatif() {
        Calculator calc = new Calculator();
        int a = -1;
        int b = -2;
        int result = a - b;
        if (calc.substract(a, b) == result) {
            System.out.println("a and b negatif ");
        }
    }
}