public class ProgrammedExceptionHandler {
    // `divideByZero` method deliberately attempts to divide by zero, which results in an ArithmeticException. 
    // The `try-catch` block is used to catch this specific exception and handle it accordingly.
    public static void main(String[] args) {
        try {
            // Code that may throw a specific exception
            int result = divideByZero(); // Example method that may throw ArithmeticException
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            // Handling the specific exception
            System.err.println("Caught an ArithmeticException: " + e.getMessage());
            // Forward error recovery - provide an alternative or log the error
        }
    }

    private static int divideByZero() {
        return 10 / 0; // This will throw an ArithmeticException
    }
}
