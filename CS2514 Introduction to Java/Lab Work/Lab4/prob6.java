import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;

public class prob6 {
    public static void main(String[] args) {
        int[][][] mat3d = new int[3][3][3];

        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    mat3d[i][j][k] = ThreadLocalRandom.current().nextInt(0, 100 + 1);
                }
            }
        }

        Scanner sc = new Scanner(System.in);
        System.out.print("Number: ");
        int guess = sc.nextInt();
        sc.close();

        boolean in_matrix = false;

        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    if (mat3d[i][j][k] == guess){
                        in_matrix = true;
                    }
                    System.out.print("|" + mat3d[i][j][k] + "|");
                }
                System.out.println();
            }
            System.out.println("----------");
        }

        System.out.println(in_matrix);
    }
}
