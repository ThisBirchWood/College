import java.util.Scanner;

public class prob2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Length of: ");
        int length = sc.nextInt();

        int[] nums = new int[length];
        int sum = 0;
        int mean;

        System.out.println("Input " + length + " numbers: ");
        for (int i = 0; i < length; i++){
            int n = sc.nextInt();
            nums[i] = n;
            sum += n;
        }
        sc.close();

        mean = sum/length;

        int stand = 0;

        for (int i = 0; i < length; i++){
            stand += Math.pow((nums[i] - mean), 2);
        }

        Double standard_deviation = Math.sqrt(stand/length);

        System.out.println("Standard Deviation: " + standard_deviation);
    }
}
