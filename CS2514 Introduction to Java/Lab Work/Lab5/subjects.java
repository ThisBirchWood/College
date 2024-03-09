import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class subjects {
    public static void main(String[] args) {
        // setup list
        ArrayList<String> subjects = new ArrayList<String>();

        // setup user input, ask for number of subjects and ask for subjects
        Scanner sc = new Scanner(System.in); //setup a scanner object
        System.out.print("Number of subjects: ");   // ask user for a number of subjects
        int length = sc.nextInt();  // scan number of subjects inputted
        sc.nextLine();      // to go next line to avoid being on the same line
        System.out.println("Give computer science subjects: "); // ask user for N subjects

        // loop N times to ask for input
        for (int i = 0; i < length; i++){  
            subjects.add(sc.nextLine());    // add each line to the array
        }
        sc.close(); // close canner

        // loop through arraylist until we find "networking" and remove it
        for (int i = 0; i < subjects.size() ; i++){
            if (subjects.get(i).toLowerCase().equals("networking")){    // check if lower case is equal to networking
                subjects.remove(i); // if it is remove it
                i -= 1;     // move i back by one because the length of the list has reduced
            }
        }

        // sort and reverse list, then print
        Collections.sort(subjects, String.CASE_INSENSITIVE_ORDER);  // sort the list, ignore case
        Collections.reverse(subjects);  // reverse the list
        System.out.println(subjects);   // print the list

    }
}