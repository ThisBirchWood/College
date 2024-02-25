import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;

public class prob6 {
    public static void main(String[] args) {
        // declare a 3d array of length, width and height of 3
        int[][][] mat3d = new int[3][3][3];

        // triped nested for loop to loop through each cell and assign a random value to it
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    mat3d[i][j][k] = ThreadLocalRandom.current().nextInt(0, 100 + 1);
                }
            }
        }

        // ask user for a number
        Scanner sc = new Scanner(System.in);
        System.out.print("Number: ");
        int guess = sc.nextInt();
        sc.close();

        // bool that defaults to false
        boolean in_matrix = false;

        // loop through the matrix again to check if the number given is there
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    // if the current cell in the array is equal to given number, set bool value to true
                    if (mat3d[i][j][k] == guess){
                        in_matrix = true;
                    }
                    System.out.print("|" + mat3d[i][j][k] + "|");
                }
                System.out.println();
            }
            System.out.println("----------");
        }
        // print whether it was in the 3d array or not
        System.out.println(in_matrix);
    }
}
