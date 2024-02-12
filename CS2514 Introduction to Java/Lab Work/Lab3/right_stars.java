public class right_stars {
    public static void main(String[] args){
        int rows = 6;
        for (int i = 1; i < rows; i++){
            System.out.println(stars(i));
        }
    }

    private static String stars(int amount){
        String s = "";
        for(int i = 0; i < amount; i++){
            s += "*";
        }
        return s;
    }
}
