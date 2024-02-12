import java.util.Scanner;
import java.util.ArrayList;

public class perfect_number {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Number between 20 and 30: ");
        int num = sc.nextInt();
        sc.close();

        if (num < 20 || num > 30){
            System.out.println("Number must be between 20 and 30!");
        } else {
            ArrayList<Integer> divisors = get_divisors(num);
            int sum = 0;

            for(int i=0; i < divisors.size(); i++){
                sum += divisors.get(i);
            }

            if (sum == num){
                System.out.println(divisors + " does equal " + num + ". It is a perfect number");
            } else {
                System.out.println(divisors + " does not equal " + num + ". It is not a perfect number");
            }
        }
    }

    private static ArrayList<Integer> get_divisors(int x){
        ArrayList<Integer> divisors = new ArrayList<Integer>();
        for (int i = 1; i < x; i++){
            if ((x % i) == 0){
                divisors.add(i);
            }
        }

        return divisors;
    }
}
