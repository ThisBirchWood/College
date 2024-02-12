
public class left_stars {
    public static void main(String[] args) {
        int rows = 6;

        for (int i = 1; i <= rows; i++){
            System.out.println(stars(i, rows));
        }
        
    }

    private static String stars(int amount, int length){
        String s = "";
        int start_index = length - amount;

        for(int i = 0; i < length; i++){
            if (i >= start_index) {
                s += "*";
            } else {
                s += " ";
            }
        }
        return s;
    }
}
