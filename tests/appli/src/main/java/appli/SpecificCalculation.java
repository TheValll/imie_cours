package appli;

public class SpecificCalculation {
    protected ICalculator creerCalculator(){
        return new Calculator();
    }

    public int addsub(int a, int b, int c) {
        ICalculator calc = creerCalculator();
        int result = calc.substract(calc.add(a, b), c);
        return result;
    }
}
