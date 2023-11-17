public class DefaultExceptionHandlingExample {
    // the `try-catch` block catches a general Exception instead of a specific one. This is considered a catch-all handler 
    // for unexpected exceptions. 
    public static void main(String[] args) {
        try {
            // Code that may throw a specific exception
            int result = divideByZero(); // Example method that may throw ArithmeticException
            System.out.println("Result: " + result);
        } catch (Exception e) {
            // Catch-all handler for unexpected exceptions
            System.err.println("Caught an unexpected exception: " + e.getMessage());
            // Log the error or perform necessary actions for recovery
        }
    }

    private static int divideByZero() {
        return 10 / 0; // This will throw an ArithmeticException
    }
}
