import java.util.Scanner;

public class prob4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // declare 2 2d arrays to store the matricies
        int[][] mat1 = new int[3][3];
        int[][] mat2 = new int[3][3];

        System.out.println("MATRIX 1");
        // loop for each row
        for (int i = 0; i < 3; i++){
            int d = i + 1;
            // loop to get the user input for nums in the given row
            System.out.println("Enter 3 nums for row " + d);
            for(int j = 0; j < 3; j++){
                int n = sc.nextInt();
                mat1[i][j] = n; // add to the first matrix
            }
        }

        // this is the same as the first loop but instead adds to the second matrix
        System.out.println("MATRIX 2");
        for (int i = 0; i < 3; i++){
            int d = i + 1;
            System.out.println("Enter 3 nums for row " + d);
            for(int j = 0; j < 3; j++){
                int n = sc.nextInt();
                mat2[i][j] = n;
            }
        }

        // declare another 2d array to store the result
        int[][] result = new int[3][3];

        System.out.println("RESULT MATRIX");
        // nested for loop to loop through each cell in the 2d array and add the two matricies together into the result matrix
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                result[i][j] = mat1[i][j] + mat2[i][j];
                // print result for this cell
                System.out.print("|" + result[i][j] + "|");
            }
            // move to another line to represent the next row
            System.out.println();
        }

        sc.close();
    }
}
