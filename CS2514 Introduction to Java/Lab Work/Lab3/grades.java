import java.util.Scanner;
import java.util.ArrayList;

public class grades {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of students: ");
        int no_of_students = sc.nextInt();
        sc.nextLine();

        ArrayList<String> names = new ArrayList<String>();
        ArrayList<Integer> marks = new ArrayList<Integer>();

        int sum_marks = 0;

        for (int i = 0; i < no_of_students; i++){
            System.out.print("Name of Student " + (i+1) + ": ");
            String name = sc.nextLine();
            System.out.print("Marks of student " + (i+1) + ": ");
            int mark = sc.nextInt();
            sc.nextLine();

            names.add(name);
            marks.add(mark);
            sum_marks += mark;
        }

        sc.close();

        for (int i = 0; i < no_of_students; i++){
            String name = names.get(i);
            String grade = get_grade(marks.get(i));

            System.out.println("Name: " + name + " - Grade: " + grade);
        }

        System.out.println("Average mark for class: " + (sum_marks/no_of_students));


    }

    private static String get_grade(int grade){
        if (grade >= 80){
            return "A";
        } else if (grade >= 60){
            return "B";
        } else if (grade >= 40){
            return "C";
        } else {
            return "D";
        }
    }
}
