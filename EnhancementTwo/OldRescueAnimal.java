import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Driver {
    // Creating ArrayLists for different animal types
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();
    private static ArrayList<Bird> birdList = new ArrayList<Bird>();
    private static ArrayList<Reptile> reptileList = new ArrayList<Reptile>();

    public static void main(String[] args) {
        // Initializing the lists with some pre-defined animals
        initializeDogList();
        initializeMonkeyList();
        initializeBirdList();
        initializeReptileList();

        Scanner input = new Scanner(System.in);
        int option;

        // Displaying the menu in a loop until the user exits
        do {
            displayMenu();
            // Ensuring valid integer input for the menu option
            while (true) {
                try {
                    option = input.nextInt();
                    break;
                } catch (InputMismatchException e) {
                    System.out.println("Invalid input. Please enter a number between 1 and 7.");
                    input.next();
                }
            }

            // Handling menu options
            switch (option) {
                case 1 -> intakeNewDog(input);
                case 2 -> intakeNewMonkey(input);
                case 3 -> reserveAnimal(input);
                case 4 -> printDogs();
                case 5 -> printMonkeys();
                case 6 -> printAvailableAnimals();
                case 7 -> System.out.println("You Exited the application. Good Bye!!!");
                default -> System.out.println("Invalid menu choice. Please try again...");
            }
        } while (option != 7);
    }

    // Method to display the menu options
    public static void displayMenu() {
        System.out.println("\n\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[7] Quit the application");
        System.out.println("Enter a menu selection: ");
    }

    // Method to initialize the dog list with some dogs
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");
        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }

    // Method to initialize the monkey list with some monkeys
    public static void initializeMonkeyList() {
        Monkey mon1 = new Monkey("Mony", "Capuchin Monkey", "male", "1", "9", "04-12-2019", "United States", "intake", false, "United States");
        Monkey mon2 = new Monkey("Rexon", "Squirrel Monkey", "male", "5", "18.4", "02-03-2020", "United States", "intake", false, "United States");
        Monkey mon3 = new Monkey("Della", "Spider Monkey", "female", "6", "25.6", "12-12-2019", "Canada", "in service", false, "Canada");
        monkeyList.add(mon1);
        monkeyList.add(mon2);
        monkeyList.add(mon3);
    }

    // Method to initialize the bird list with some birds
    public static void initializeBirdList() {
        Bird bird1 = new Bird("Tweety", "Parrot", "female", "2", "0.5", "01-10-2021", "Australia", "intake", false, "Australia");
        Bird bird2 = new Bird("Sky", "Sparrow", "male", "1", "0.2", "11-11-2020", "United States", "Phase I", false, "United States");
        birdList.add(bird1);
        birdList.add(bird2);
    }

    // Method to initialize the reptile list with some reptiles
    public static void initializeReptileList() {
        Reptile reptile1 = new Reptile("Slinky", "Iguana", "male", "3", "1.5", "07-12-2019", "Brazil", "in service", false, "Brazil");
        Reptile reptile2 = new Reptile("Creepy", "Snake", "female", "4", "2.1", "03-04-2020", "India", "Phase II", false, "India");
        reptileList.add(reptile1);
        reptileList.add(reptile2);
    }

    // Method to intake a new monkey
    public static void intakeNewMonkey(Scanner scanner) {
        scanner.nextLine();
        System.out.println("What is the monkey's name?");
        String name = scanner.nextLine();
        System.out.println("What is the monkey's species type?");
        String aType = scanner.nextLine();

        // Checking if the monkey is already in the system
        for (Monkey monkey : monkeyList) {
            if (monkey.getName().equalsIgnoreCase(name) && monkey.getAnimalType().equalsIgnoreCase(aType)) {
                System.out.println("\n\nThis monkey is already in our system\n\n");
                return;
            }
        }

        // Intake details for a new monkey
        System.out.println("Enter the monkey's gender");
        String gender = scanner.nextLine();
        System.out.println("Enter the monkey's age");
        String age = scanner.nextLine();
        System.out.println("Enter the monkey's weight");
        String weight = scanner.nextLine();
        System.out.println("Enter the monkey acquisition Date");
        String aDate = scanner.nextLine();
        System.out.println("Enter the monkey acquisition country");
        String aCountry = scanner.nextLine();
        System.out.println("Enter the monkey training status");
        String status = scanner.nextLine();
        System.out.println("Enter the monkey reserved status (true/false)");
        boolean reserved = scanner.nextBoolean();
        scanner.nextLine();
        System.out.println("Enter the monkey in service country name");
        String serCountry = scanner.nextLine();

        Monkey mon1 = new Monkey(name, aType, gender, age, weight, aDate, aCountry, status, reserved, serCountry);
        monkeyList.add(mon1);
    }

    // Method to intake a new dog
    public static void intakeNewDog(Scanner scanner) {
        scanner.nextLine();
        System.out.println("What is the dog name?");
        String name = scanner.nextLine();

        // Checking if the dog is already in the system
        for (Dog dog : dogList) {
            if (dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return;
            }
        }

        // Intake details for a new dog
        System.out.println("Enter the dog type");
        String aType = scanner.nextLine();
        System.out.println("Enter the dog gender");
        String gender = scanner.nextLine();
        System.out.println("Enter the dog age");
        String age = scanner.nextLine();
        System.out.println("Enter the dog weight");
        String weight = scanner.nextLine();
        System.out.println("Enter the dog acquisition Date");
        String aDate = scanner.nextLine();
        System.out.println("Enter the dog acquisition country");
        String aCountry = scanner.nextLine();
        System.out.println("Enter the dog training status");
        String status = scanner.nextLine();
        System.out.println("Enter the dog reserved status (true/false)");
        boolean reserved = scanner.nextBoolean();
        scanner.nextLine();
        System.out.println("Enter the dog in service country name");
        String serCountry = scanner.nextLine();

        Dog dog1 = new Dog(name, aType, gender, age, weight, aDate, aCountry, status, reserved, serCountry);
        dogList.add(dog1);
    }

    // Method to reserve an animal
    public static void reserveAnimal(Scanner scanner) {
        scanner.nextLine();
        System.out.println("Enter the desired animal Type:");
        String aType = scanner.nextLine();
        System.out.println("Enter the desired country name:");
        String country = scanner.nextLine();

        // Reserving a dog if available
        for (Dog dog : dogList) {
            if (dog.getAnimalType().equalsIgnoreCase(aType) && dog.getInServiceCountry().equalsIgnoreCase(country) && !dog.isReserved()) {
                dog.setReserved(true);
                System.out.println("Animal is reserved successfully");
                return;
            }
        }

        // Reserving a monkey if available
        for (Monkey mon : monkeyList) {
            if (mon.getAnimalType().equalsIgnoreCase(aType) && mon.getInServiceCountry().equalsIgnoreCase(country) && !mon.isReserved()) {
                mon.setReserved(true);
                System.out.println("Animal is reserved successfully");
                return;
            }
        }

        // Reserving a bird if available
        for (Bird bird : birdList) {
            if (bird.getAnimalType().equalsIgnoreCase(aType) && bird.getInServiceCountry().equalsIgnoreCase(country) && !bird.isReserved()) {
                bird.setReserved(true);
                System.out.println("Animal is reserved successfully");
                return;
            }
        }

        // Reserving a reptile if available
        for (Reptile reptile : reptileList) {
            if (reptile.getAnimalType().equalsIgnoreCase(aType) && reptile.getInServiceCountry().equalsIgnoreCase(country) && !reptile.isReserved()) {
                reptile.setReserved(true);
                System.out.println("Animal is reserved successfully");
                return;
            }
        }

        // If no animal is available for the given type and location
        System.out.println("No animal Type and location of your desired choice is available");
    }

    // Method to print all dogs
    public static void printDogs() {
        System.out.println("Dog Details");
        System.out.println("-----------------------------------");
        for (Dog dog : dogList) {
            System.out.println(dog);
        }
    }

    // Method to print all monkeys
    public static void printMonkeys() {
        System.out.println("Monkey Details");
        System.out.println("-----------------------------------");
        for (Monkey mon : monkeyList) {
            System.out.println(mon);
        }
    }

    // Method to print all available animals (not reserved and in service)
    public static void printAvailableAnimals() {
        System.out.println("Displaying all Available Animals");
        System.out.println("-----------------------------------");

        for (Dog dog : dogList) {
            if (!dog.isReserved() && dog.getTrainingstatus().equalsIgnoreCase("in service")) {
                System.out.println(dog);
            }
        }

        for (Monkey mon : monkeyList) {
            if (!mon.isReserved() && mon.getTrainingstatus().equalsIgnoreCase("in service")) {
                System.out.println(mon);
            }
        }

        for (Bird bird : birdList) {
            if (!bird.isReserved() && bird.getTrainingstatus().equalsIgnoreCase("in service")) {
                System.out.println(bird);
            }
        }

        for (Reptile reptile : reptileList) {
            if (!reptile.isReserved() && reptile.getTrainingstatus().equalsIgnoreCase("in service")) {
                System.out.println(reptile);
            }
        }
    }
}

// Base class for all rescue animals
public class RescueAnimal {
    private String name;
    private String animalType;
    private String gender;
    private String age;
    private String weight;
    private String acquisitionDate;
    private String acquisitionCountry;
    private String trainingstatus;
    private boolean reserved;
    private String inServiceCountry;

    public RescueAnimal(String n, String aT, String g, String a, String w, String aDate, String aCountry, String status, boolean res, String serCountry) {
        name = n;
        animalType = aT;
        gender = g;
        age = a;
        weight = w;
        acquisitionDate = aDate;
        acquisitionCountry = aCountry;
        trainingstatus = status;
        reserved = res;
        inServiceCountry = serCountry;
    }

    public String getName() {
        return name;
    }

    public String getAnimalType() {
        return animalType;
    }

    public String getGender() {
        return gender;
    }

    public String getAge() {
        return age;
    }

    public String getWeight() {
        return weight;
    }

    public String getAcquisitionDate() {
        return acquisitionDate;
    }

    public String getAcquisitionCountry() {
        return acquisitionCountry;
    }

    public String getTrainingstatus() {
        return trainingstatus;
    }

    public boolean isReserved() {
        return reserved;
    }

    public String getInServiceCountry() {
        return inServiceCountry;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAnimalType(String animalType) {
        this.animalType = animalType;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public void setAcquisitionDate(String acquisitionDate) {
        this.acquisitionDate = acquisitionDate;
    }

    public void setAcquisitionCountry(String acquisitionCountry) {
        this.acquisitionCountry = acquisitionCountry;
    }

    public void setTrainingstatus(String trainingstatus) {
        this.trainingstatus = trainingstatus;
    }

    public void setReserved(boolean reserved) {
        this.reserved = reserved;
    }

    public void setInServiceCountry(String inServiceCountry) {
        this.inServiceCountry = inServiceCountry;
    }

    @Override
    public String toString() {
        return String.format("Name: %s\nAcquisitionCountry: %s\nTrainingstatus: %s\nReserved: %s", name, acquisitionCountry, trainingstatus, reserved);
    }
}

// Dog class inheriting from RescueAnimal
public class Dog extends RescueAnimal {
    public Dog(String n, String aT, String g, String a, String w, String aDate, String aCountry, String status, boolean res, String serCountry) {
        super(n, aT, g, a, w, aDate, aCountry, status, res, serCountry);
    }
}

// Monkey class inheriting from RescueAnimal
public class Monkey extends RescueAnimal {
    public Monkey(String n, String aT, String g, String a, String w, String aDate, String aCountry, String status, boolean res, String serCountry) {
        super(n, aT, g, a, w, aDate, aCountry, status, res, serCountry);
    }
}

// Bird class inheriting from RescueAnimal
public class Bird extends RescueAnimal {
    public Bird(String n, String aT, String g, String a, String w, String aDate, String aCountry, String status, boolean res, String serCountry) {
        super(n, aT, g, a, w, aDate, aCountry, status, res, serCountry);
    }
}

// Reptile class inheriting from RescueAnimal
public class Reptile extends RescueAnimal {
    public Reptile(String n, String aT, String g, String a, String w, String aDate, String aCountry, String status, boolean res, String serCountry) {
        super(n, aT, g, a, w, aDate, aCountry, status, res, serCountry);
    }
}
