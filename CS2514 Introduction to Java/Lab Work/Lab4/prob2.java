import java.util.Scanner;

public class prob2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Length of: "); // ask for amount of numbers
        int length = sc.nextInt();  // get that number

        // declare length array, sum and mean vars
        int[] nums = new int[length];
        int sum = 0;
        int mean;

        // tell user to input numbers
        System.out.println("Input " + length + " numbers: ");
        // loop
        for (int i = 0; i < length; i++){
            int n = sc.nextInt(); // ask for next int
            nums[i] = n;    // add to array
            sum += n;   // add to sum var
        }
        sc.close();

        // get mean of all numbers
        mean = sum/length;


        int stand = 0;

        for (int i = 0; i < length; i++){
            stand += Math.pow((nums[i] - mean), 2); // add sd formula to a counter
        }

        // declare standard devation by getting the square root
        Double standard_deviation = Math.sqrt(stand/length);


        // display it 
        System.out.println("Standard Deviation: " + standard_deviation);
    }
}
