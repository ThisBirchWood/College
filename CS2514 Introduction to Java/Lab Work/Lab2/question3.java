public class question3 {
    public static void main(String[] args){
        gravity(50);
    }
    public static void gravity(int weight){
        System.out.println("Mercury: " + weight*0.4);
        System.out.println("Venus: " + weight*0.9);
        System.out.println("Jupiter: " + weight*2.5);
        System.out.println("Saturn: " + weight*1.1);
    }
}
