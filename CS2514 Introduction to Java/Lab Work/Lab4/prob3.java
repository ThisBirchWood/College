import java.util.Scanner;
import java.util.Arrays;

public class prob3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 10 names: ");
        String[] names = new String[10];

        for(int i = 0; i < 10; i++){
            names[i] = sc.nextLine();
        }
        sc.close();

        Arrays.sort(names, String.CASE_INSENSITIVE_ORDER);

        System.out.println(Arrays.toString(names));

    }
}
