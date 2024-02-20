import java.util.Scanner;

public class prob5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Width of matrix: ");
        int width = sc.nextInt();

        System.out.print("Length of matrix:");
        int length = sc.nextInt();

        int[][] mat = new int[length][width];

        for (int i = 0; i < length; i++){
            int d = i + 1;
            System.out.println("Enter " + width + " nums for row " + d);
            for(int j = 0; j < width; j++){
                int n = sc.nextInt();
                mat[i][j] = n;
            }
        }
        sc.close();

        System.out.println("Transpose:");

        for (int i = 0; i < width; i++){
            for (int j = 0; j < length; j++){
                System.out.print("|" + mat[j][i] + "|");
            }
            System.out.println();
        }
    }
}
