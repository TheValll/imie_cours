package appli;

import org.junit.Test;

import static org.junit.Assert.*;

public class SpecificCalculationTest {

    @Test
    public void addsub() {
        Calculator calc = new Calculator();
        SpecificCalculation specificCalculation = new SpecificCalculation();
        int a = 1;
        int b = 2;
        int c = 3;
        int result = a + b - c;

        if(specificCalculation.addsub(a, b, c) != result){
            fail("addsub");
        }
    }

    @Test
    public void test1AvecMock() {
        SpecificCalculation calc = new SpecificCalculation(){
            protected ICalculator creerCalculator(){
                return new MockCalculator();
            }
        };
        int a=-5, b=10, c=10, res;
        res = a + b - c;
        assertTrue("a négatif, b positif, c positif", calc.addsub(a, b, c) == res);
    }
}