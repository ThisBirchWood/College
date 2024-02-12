import java.util.Scanner;

public class coffee {
    public static void main(String[] args){
        double pricePerPound = 5.99;
        double tax = 0.0725;
        double totalPrice;
        double totalPriceWithTax;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Number of bags sold: ");
        int numberOfUnits = scanner.nextInt();
        System.out.print("Weight per bag: ");
        int unitWeight = scanner.nextInt();
        scanner.close();

        totalPrice = unitWeight * numberOfUnits * pricePerPound;
        totalPriceWithTax = totalPrice + (totalPrice * tax);

        System.out.println("Price per pound: $" + pricePerPound);
        System.out.println("Sales Tax: " + tax*100 + "%");
        System.out.println("Total price: $" + totalPriceWithTax);
    }
}
