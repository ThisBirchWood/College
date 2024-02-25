import java.util.Scanner;
import java.util.Arrays;

public class prob3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 10 names: "); // ask for 10 names
        String[] names = new String[10]; // make string array of length 10

        // loop 10 times to ask for names
        for(int i = 0; i < 10; i++){
            names[i] = sc.nextLine();
        }
        sc.close();

        // sort the array without caring about case
        Arrays.sort(names, String.CASE_INSENSITIVE_ORDER);

        // print the array
        System.out.println(Arrays.toString(names));

    }
}
