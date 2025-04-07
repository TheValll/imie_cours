package appli;

public class Calculator implements  ICalculator {

    @Override
    public int multiply(int a, int b) {
        int result = 0;
        int absA = Math.abs(a);
        int absB = Math.abs(b);

        for (int i = 0; i < absB; i++) {
            result += absA;
        }

        if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
            result = -result;
        }

        return result;
    }

    @Override
    public int divide(int a, int b) {
        return a / b;
    }

    @Override
    public int add(int a, int b) {
        int result = a;
        int absB = Math.abs(b);

        for (int i = 0; i < absB; i++) {
            if (b > 0) {
                result++;
            } else {
                result--;
            }
        }
        return result;
    }

    @Override
    public int substract(int a, int b) {
        int result = a;
        int absB = Math.abs(b);
        for (int i = 0; i < absB; i++) {
            if (b > 0) {
                result--;
            } else {
                result++;
            }
        }
        return result;
    }
}
