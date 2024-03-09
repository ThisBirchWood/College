import java.util.HashMap;
import java.util.Scanner;

public class hash {
    public static void main(String[] args) {
        // setup hash map, with integer key and string value
        HashMap<Integer, String> players = new HashMap<Integer, String>();

        // add all values, random names
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

        // setup user input and read it
        Scanner sc = new Scanner(System.in);    // setup scanner
        System.out.print("Give player number: ");   // print "Give player number: " to the terminal
        int player_key = sc.nextInt();  // scan what integer the user inputted and store it
        sc.close(); // close scanner

        // print value based of the key the user gave
        System.out.println(players.get(player_key));

    }
}
