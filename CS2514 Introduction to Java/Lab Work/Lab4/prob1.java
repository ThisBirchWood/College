import java.util.Scanner;

public class prob1 {
    public static void main(String[] args) {
        int even = 0;
        int odd = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 10 numbers: ");
        for (int i = 0; i < 10; i++){
            int num = sc.nextInt();

            if ((num % 2) == 0){
                even += 1;
            } else {
                odd += 1;
            }
        }

        sc.close();

        System.out.println("Even nums: " + even);
        System.out.println("Odd nums: " + odd);
    }
}