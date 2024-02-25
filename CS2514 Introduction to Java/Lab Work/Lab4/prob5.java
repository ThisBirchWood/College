import java.util.Scanner;

public class prob5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // get user input for width of matrix
        System.out.print("Width of matrix: ");
        int width = sc.nextInt();

        // get user input for length of matrix
        System.out.print("Length of matrix:");
        int length = sc.nextInt();

        // declare a 2d array of given width and length
        int[][] mat = new int[length][width];

        // loop each row of the matrix
        for (int i = 0; i < length; i++){
            // d is the row number
            int d = i + 1;
            System.out.println("Enter " + width + " nums for row " + d);
            // loop through each column and ask for the value in the row and column cell
            for(int j = 0; j < width; j++){
                int n = sc.nextInt();
                mat[i][j] = n; // add to matrix
            }
        }
        sc.close();

        System.out.println("Transpose:");
        // loop through the columns first because we are getting the transpose
        for (int i = 0; i < width; i++){
            for (int j = 0; j < length; j++){
                // print the cell in opposite order to show the transpose
                System.out.print("|" + mat[j][i] + "|");
            }
            // go to new line to represent a new row
            System.out.println();
        }
    }
}
