import java.util.Scanner;

public class prob4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] mat1 = new int[3][3];
        int[][] mat2 = new int[3][3];

        System.out.println("MATRIX 1");
        for (int i = 0; i < 3; i++){
            int d = i + 1;
            System.out.println("Enter 3 nums for row " + d);
            for(int j = 0; j < 3; j++){
                int n = sc.nextInt();
                mat1[i][j] = n;
            }
        }

        System.out.println("MATRIX 2");
        for (int i = 0; i < 3; i++){
            int d = i + 1;
            System.out.println("Enter 3 nums for row " + d);
            for(int j = 0; j < 3; j++){
                int n = sc.nextInt();
                mat2[i][j] = n;
            }
        }

        int[][] result = new int[3][3];

        System.out.println("RESULT MATRIX");
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                result[i][j] = mat1[i][j] + mat2[i][j];
                System.out.print("|" + result[i][j] + "|");
            }
            System.out.println();
        }

        sc.close();
    }
}
