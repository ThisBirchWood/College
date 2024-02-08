public class question6 {
    public static void main(String[] args){
        System.out.println(can_donate(19, 50)); // alice
        System.out.println(can_donate(20, 36)); // bob
        System.out.println(can_donate(17, 45)); // clive
    }
    public static boolean can_donate(int age, int weight){
        if ((age >= 18 && age <= 60) && weight >= 40){
            return true;
        } else {
            return false;
        }
    }
}
