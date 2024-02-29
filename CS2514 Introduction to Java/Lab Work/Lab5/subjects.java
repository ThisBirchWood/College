import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class subjects {
    public static void main(String[] args) {
        ArrayList<String> subjects = new ArrayList<String>();

        Scanner sc = new Scanner(System.in);
        System.out.print("Number of subjects: ");
        int length = sc.nextInt();
        sc.nextLine();
        System.out.println("Give computer science subjects: ");

        for (int i = 0; i < length; i++){
            subjects.add(sc.nextLine());
        }
        sc.close();

        System.out.println(subjects);

        for (int i = 0; i < subjects.size() ; i++){
            if (subjects.get(i).toLowerCase().equals("networking")){
                subjects.remove(i);
                i -= 1;
            }
        }

        Collections.sort(subjects, String.CASE_INSENSITIVE_ORDER);
        Collections.reverse(subjects);
        System.out.println(subjects);

    }
}