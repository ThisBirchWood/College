import java.util.Scanner;

public class diamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Amount of rows: ");
        int rows = sc.nextInt();
        sc.close();

        StringBuilder s = new StringBuilder();
        s.repeat(" ", rows+1);

        int i;
        int j;

        if ((rows % 2) == 0){
            i = rows/2;
            j = (rows/2)+1;
        } else {
            i = (rows+1)/2;
            j = (rows+1)/2;
        }


        while ((j <= rows) && (i >= 0)){
            s.setCharAt(i, '*');
            s.setCharAt(j, '*');

            i -= 1;
            j += 1;

            System.out.println(s);
        }

        if ((rows % 2) == 0){
            System.out.println(s);
        }

        while (i < j) {  
            i += 1;
            j -= 1;

            s.setCharAt(i, ' ');
            s.setCharAt(j, ' ');

            System.out.println(s);
        }
    }
}
