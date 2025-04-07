package appli;

public class Calculator implements  ICalculator {

    @Override
    public int multiply(int a, int b) {
        int result = 0;
        for (int i = 0; i < b; i++) {
            result = add(result, a);
        }
        return result;
    }

    @Override
    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed.");
        }
        int result = 0;
        int sum = 0;
        while (sum < a) {
            sum = add(sum, b);
            if (sum <= a) {
                result++;
            }
        }
        return result;
    }

    @Override
    public int add(int a, int b) {
        for(int i =0; i<a; i++) {
            b++;
        }

        return b;
    }

    @Override
    public int substract(int a, int b) {
        for(int i =0; i<a; i++) {
            b--;
        }

        return b;
    }
}
