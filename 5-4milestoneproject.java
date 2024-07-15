import java.util.ArrayList;
import java.util.Scanner;
/** This class test the functionality of Dog and Monkey classes **/
public class Driver {
//creating an arraylist for dog and monkey
        private static ArrayList<Dog> dogList=new ArrayList<Dog>();
        private static ArrayList<Monkey> monkeyList=new ArrayList<Monkey>();
        public static void main(String[] args) {
//calls the method to initialize the arraylist
        initializeDogList();
        initializeMonkeyList();
//create a scanner class object
        Scanner input=new Scanner(System.in);
        int option;
//displaying the menu in loop until the user enters the exit option
        do{
displayMenu();
option=input.nextInt();
//if the option is 1 call the intakeNewDog() method with scanner object as parameter
if(option==1)
{
intakeNewDog(input);
}
//if the option is 2 call the intakeNewMonkey() method with scanner object as parameter
else if(option==2)
{
intakeNewMonkey(input);
}
//if the option is 3 call the reserveAnimal() method with scanner object as parameter
else if(option==3)
{
reserveAnimal(input);
}
//if the option is 4 call the printDogs() method
else if(option==4)
{
printDogs();
}
//if the option is 5 call the printMonkeys() method
else if(option==5)
{
printMonkeys();
}
//if the option is 6 call the printAvailableAnimals() method
else if(option==6)
{
printAvailableAnimals();
}
//if the option is 7, then display the message and exit the loop
else if(option==7)
{
System.out.println("You Exited the application. Good Bye!!!");
break;
}
//if the user option is invalid, then display the error message and continue the loop
else
{
System.out.println("Invalid menu choice. Please try again....");
continue;
}
}while(option!=7);

}
//this method displays the menu option to the user
public static void displayMenu()
{
System.out.println("\n");
System.out.println("\t\t\tRescue Animal System Menu");
System.out.println("[1] Intake a new dog");
System.out.println("[2] Intake a new monkey");
System.out.println("[3] Reserve an animal");
System.out.println("[4] Print a list of all dogs");
System.out.println("[5] Print a list of all monkeys");
System.out.println("[6] Print a list of all animals that are not reserved");
System.out.println("[7] Quit the application");
System.out.println("\n");
System.out.println("Enter a menu selection: ");
}
//this method initializes several dog objects and add it to the arraylist dogList
public static void initializeDogList()
{
Dog dog1=new Dog("Spot","German Shephered","male","1","25.6","05-12-2019","united states","intake",false,"United States");
Dog dog2=new Dog("Rex","Great Dane","male","3","35.2","02-03-2020","united states","Phase I",false,"United States");
Dog dog3=new Dog("Bella","Chihuahua","female","4","25.6","12-12-2019","Canada","in service",true,"Canada");
dogList.add(dog1);
dogList.add(dog2);
dogList.add(dog3);
}
//this method initializes several monkey objects and add it to the arraylist monkeyList
public static void initializeMonkeyList()
{
Monkey mon1=new Monkey("Mony","Capuchin Monkey","male","1","9","04-12-2019","united states","intake",false,"United States");
Monkey mon2=new Monkey("Rexon","Squirrel Monkey","male","5","18.4","02-03-2020","united states","intake",false,"United States");
Monkey mon3=new Monkey("Della","Spider Monkey","female","6","25.6","12-12-2019","Canada","in service",false,"Canada");
monkeyList.add(mon1);
monkeyList.add(mon2);
monkeyList.add(mon3);
}
//this method adds the new monkey to the arraylist if the monkey name and its species type is not already there in the list
public static void intakeNewMonkey(Scanner scanner)
{
scanner.nextLine();
System.out.println("What is the monkey's name? ");
String name=scanner.nextLine();
System.out.println("What is the monkey's species type? ");
String aType=scanner.nextLine();
//validating the user input of name and species with the entries in arraylist
for(Monkey monkey:monkeyList)
{
//if the entry is already there, then display the message and return the control to the menu
if(monkey.getName().equalsIgnoreCase(name)&&monkey.getAnimalType().equalsIgnoreCase(aType))
{
System.out.println("\n\nThis monkey is already in our system\n\n");
return;
}
}
//else, asks for the input for other attributes of monkey object
System.out.println("Enter the monkey's gender ");
String gender=scanner.nextLine();
System.out.println("Enter the monkey's age ");
String age=scanner.nextLine();
System.out.println("Enter the monkey's weight ");
String weight=scanner.nextLine();
System.out.println("Enter the monkey acquisition Date ");
String aDate=scanner.nextLine();
System.out.println("Enter the monkey acquisition country ");
String aCountry=scanner.nextLine();
System.out.println("Enter the monkey training status ");
String status=scanner.nextLine();
System.out.println("Enter the monkey reserved status (true/false) ");
boolean reserved=scanner.nextBoolean();
scanner.nextLine();
System.out.println("Enter the monkey in service country name ");
String serCountry=scanner.nextLine();
//instantiate an object for monkey with user inputs and add it to the arraylist
Monkey don1=new Monkey(name,aType,gender,age,weight,aDate,aCountry,status,reserved,serCountry);
monkeyList.add(don1);
}
//this method adds the dog to the arraylist dogList if the dog name is not there
public static void intakeNewDog(Scanner scanner)
{
scanner.nextLine();
System.out.println("What is the dog name? ");
String name=scanner.nextLine();
//validating the name is already there in the list, if so display the message and return to the menu
for(Dog dog:dogList)
{
if(dog.getName().equalsIgnoreCase(name))
{
System.out.println("\n\nThis dog is already in our system\n\n");
return;
}
}
//else asks for the value of other attributes and creates an object for Dog class
System.out.println("Enter the dog type ");
String aType=scanner.nextLine();
System.out.println("Enter the dog gender ");
String gender=scanner.nextLine();
System.out.println("Enter the dog age ");
String age=scanner.nextLine();
System.out.println("Enter the dog weight ");
String weight=scanner.nextLine();
System.out.println("Enter the dog acquisition Date ");
String aDate=scanner.nextLine();
System.out.println("Enter the dog acquisition country ");
String aCountry=scanner.nextLine();
System.out.println("Enter the dog training status ");
String status=scanner.nextLine();
System.out.println("Enter the dog reserved status (true/false) ");
boolean reserved=scanner.nextBoolean();
scanner.nextLine();
System.out.println("Enter the dog in service country name ");
String serCountry=scanner.nextLine();
Dog dog1=new Dog(name,aType,gender,age,weight,aDate,aCountry,status,reserved,serCountry);
//add the object to the arraylist
dogList.add(dog1);
}
//this method asks the desired animal type and location and checks the animal availability
public static void reserveAnimal(Scanner scanner)
{
scanner.nextLine();
System.out.println("Enter the desired animal Type: ");
String aType=scanner.nextLine();
System.out.println("Enter the desired country name: ");
String country=scanner.nextLine();
//if available change the reserved state to true
for(Dog dog:dogList)
{
if(dog.getAnimalType().equalsIgnoreCase(aType)&&dog.getInServiceCountry().equalsIgnoreCase(country)&&dog.isReserved()==false)
{
dog.setReserved(true);
System.out.println("Animal is reserved successfully");
return;
}

}
for(Monkey mon:monkeyList)
{
if(mon.getAnimalType().equalsIgnoreCase(aType)&&mon.getInServiceCountry().equalsIgnoreCase(country)&&mon.isReserved()==false)
{
mon.setReserved(true);
System.out.println("Animal is reserved successfully");
return;
}

}
//else display the error message
System.out.println("No animal Type and location of your desired choice is avaiable");
}
//this method displays the dog object details in arraylist dogList
public static void printDogs()
{
System.out.println("Dog Details");
System.out.println("-----------------------------------");
for(Dog dog:dogList)
System.out.println(dog.toString());
}
//this method displays the monkey object details in arraylist monkeyList
public static void printMonkeys()
{
System.out.println("Monkey Details");
System.out.println("-----------------------------------");
for(Monkey mon:monkeyList)
{
System.out.println(mon.toString());
}
}
//this method displays all available(fully trained but not reserved) animal details in both the arraylist
public static void printAvailableAnimals()
{
System.out.println("Displaying all Available Animals");
System.out.println("-----------------------------------");
for(Dog dog:dogList)
{
if(dog.isReserved()==false&&dog.getTrainingstatus().equalsIgnoreCase("in service"))
System.out.println(dog.toString());
}
for(Monkey mon:monkeyList)
{
if(mon.isReserved()==false&& mon.getTrainingstatus().equalsIgnoreCase("in service"))
System.out.println(mon.toString());
}
}

}
RescueAnimal.java

/** RescueAnimal class definition**/
public class RescueAnimal {
//instance variables
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
//constructor
public RescueAnimal(String n,String aT,String g,String a,String w,String aDate,String aCountry,String status,boolean res,String serCountry) {
name=n;
animalType=aT;
gender=g;
age=a;
weight=w;
acquisitionDate=aDate;
acquisitionCountry=aCountry;
trainingstatus=status;
reserved=res;
inServiceCountry=serCountry;
}
//getter and setter methods
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

}
Dog.java

public class Dog extends RescueAnimal{

public Dog(String n,String aT,String g,String a,String w,String aDate,String aCountry,String status,boolean res,String serCountry) {
super(n,aT,g,a,w,aDate,aCountry,status,res,serCountry);
}
public String toString() {
return(String.format("Name : " + getName() +"\nAcquisitionCountry : " + getAcquisitionCountry()
+ "\nTrainingstatus : " + getTrainingstatus() + "\nReserved : " + isReserved()));
}
}
Monkey.java

public class Monkey extends RescueAnimal{

public Monkey(String n,String aT,String g,String a,String w,String aDate,String aCountry,String status,boolean res,String serCountry) {
super(n,aT,g,a,w,aDate,aCountry,status,res,serCountry);
}

public String toString() {
return(String.format("Name : " + getName() +"\nAcquisitionCountry : " + getAcquisitionCountry()
+ "\nTrainingstatus : " + getTrainingstatus() + "\nReserved : " + isReserved()));
}


}