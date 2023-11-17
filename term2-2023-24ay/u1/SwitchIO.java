import java.util.Scanner;

public class SwitchIO {
    public enum Profession {
        SOFTWARE_ENGINEER, DATA_SCIENTIST, SOC
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your profession (SOFTWARE_ENGINEER, DATA_SCIENTIST, SOC): ");
        String userInput = scanner.nextLine();

        Profession userProfession;
        try {
            userProfession = Profession.valueOf(userInput.toUpperCase());
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid input. Please enter one of the specified professions.");
            return;
        }

        switch (userProfession) {
            case SOFTWARE_ENGINEER:
                System.out.println("You Want Problems!");
                break;
            case DATA_SCIENTIST:
                System.out.println("You Embrace Problems!");
                break;
            case SOC:
                System.out.println("You Don't want Peace!");
                break;
            default:
                System.out.println("You Ass is skeptical to aeration!");
        }
    }
}
