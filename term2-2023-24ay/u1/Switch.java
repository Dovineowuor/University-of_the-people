public class Switch {
    public enum Profession {
        SOFTWARE_ENGINEER, DATA_SCIENTIST, SOC
    }

    public static void main(String[] args) {
        Profession a = Profession;
        switch (a) {
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
                System.out.println("You Ass is sceptical to aeration!");
        }
    }
}

