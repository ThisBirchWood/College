import java.util.HashMap;
import java.util.Scanner;

public class hash {
    public static void main(String[] args) {
        HashMap<Integer, String> players = new HashMap<Integer, String>();

        players.put(1, "Bob");
        players.put(2, "Ben");
        players.put(3, "Alice");
        players.put(4, "Charlie");
        players.put(5, "David");
        players.put(6, "Eva");
        players.put(7, "Frank");
        players.put(8, "Grace");
        players.put(9, "Henry");
        players.put(10, "Ivy");

        Scanner sc = new Scanner(System.in);
        System.out.print("Give player number: ");
        int player_key = sc.nextInt();
        sc.close();

        System.out.println(players.get(player_key));

    }
}
