package appli;

import org.junit.Test;
import static org.junit.Assert.*;

public class CalculatorTest {

    @Test
    public void addABpositif() {
        Calculator calc = new Calculator();
        int a = 1;
        int b = 2;
        int result = a + b;

        if (calc.add(a, b) != result) {
            fail("add failed a b positif");
        }
    }

    @Test
    public void addABnegitif() {
        Calculator calc = new Calculator();
        int a = -1;
        int b = -2;
        int result = a + b;
        if (calc.add(a, b) != result) {
            fail("add failed a b negitif");
        }
    }

    @Test
    public void addApositifBnegitif(){
        Calculator calc = new Calculator();
        int a = 1;
        int b = -2;
        int result = a + b;
        if (calc.add(a, b) != result) {
            fail("add failed a positif b negitif");
        }
    }

    @Test
    public void addAnegatifBpositif(){
        Calculator calc = new Calculator();
        int a = -1;
        int b = 2;
        int result = a + b;
        if (calc.add(a, b) != result) {
            fail("add failed a positif b negitif");
        }
    }

    @Test
    public void substractABpositif() {
        Calculator calc = new Calculator();
        int a = 2;
        int b = 1;
        int result = a - b;

        if (calc.substract(a, b) != result) {
            fail("substract failed a b positif");
        }
    }

    @Test
    public void substractABnegitif() {
        Calculator calc = new Calculator();
        int a = -2;
        int b = -1;
        int result = a - b;
        if (calc.substract(a, b) != result) {
            fail("substract failed a b negitif");
        }
    }

    @Test
    public void substractApositifBnegitif(){
        Calculator calc = new Calculator();
        int a = 2;
        int b = -1;
        int result = a - b;
        if (calc.substract(a, b) != result) {
            fail("substract failed a positif b negitif");
        }
    }

    @Test
    public void substractAnegatifBpositif(){
        Calculator calc = new Calculator();
        int a = -2;
        int b = 1;
        int result = a - b;
        if (calc.substract(a, b) != result) {
            fail("substract failed a negatif b positif");
        }
    }

    @Test
    public void multiplyABpositif() {
        Calculator calc = new Calculator();
        int a = 2;
        int b = 3;
        int result = a * b;

        if (calc.multiply(a, b) != result) {
            fail("multiply failed a b positif");
        }
    }

    @Test
    public void multiplyABnegitif() {
        Calculator calc = new Calculator();
        int a = -2;
        int b = -3;
        int result = a * b;
        if (calc.multiply(a, b) != result) {
            fail("multiply failed a b negitif");
        }
    }

    @Test
    public void multiplyApositifBnegitif(){
        Calculator calc = new Calculator();
        int a = 2;
        int b = -3;
        int result = a * b;
        if (calc.multiply(a, b) != result) {
            fail("multiply failed a positif b negitif");
        }
    }

    @Test
    public void multiplyAnegatifBpositif(){
        Calculator calc = new Calculator();
        int a = -2;
        int b = 3;
        int result = a * b;
        if (calc.multiply(a, b) != result) {
            fail("multiply failed a negatif b positif");
        }
    }

    @Test
    public void divideABpositif() {
        Calculator calc = new Calculator();
        int a = 6;
        int b = 3;
        int result = a / b;

        if (calc.divide(a, b) != result) {
            fail("divide failed a b positif");
        }
    }

    @Test
    public void divideABnegitif() {
        Calculator calc = new Calculator();
        int a = -6;
        int b = -3;
        int result = a / b;
        if (calc.divide(a, b) != result) {
            fail("divide failed a b negitif");
        }
    }

    @Test
    public void divideApositifBnegitif(){
        Calculator calc = new Calculator();
        int a = 6;
        int b = -3;
        int result = a / b;
        if (calc.divide(a, b) != result) {
            fail("divide failed a positif b negitif");
        }
    }

    @Test
    public void divideAnegatifBpositif(){
        Calculator calc = new Calculator();
        int a = -6;
        int b = 3;
        int result = a / b;
        if (calc.divide(a, b) != result) {
            fail("divide failed a negatif b positif");
        }
    }
}
