import java.util.Scanner;

public class prob1 {
    public static void main(String[] args) {
        // declare even and odd counters
        int even = 0;
        int odd = 0;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 10 numbers: "); // ask for 10 nums
        // loop 10 times to ask for 10 numbers
        for (int i = 0; i < 10; i++){
            // get user input
            int num = sc.nextInt();

            // check if it's odd or even and add to counter
            if ((num % 2) == 0){
                even += 1;
            } else {
                odd += 1;
            }
        }

        // close scanner
        sc.close();

        // display amount of even and odd numbers
        System.out.println("Even nums: " + even);
        System.out.println("Odd nums: " + odd);
    }
}