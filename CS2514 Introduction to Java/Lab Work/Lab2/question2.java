public class question2 {
    public static void main(String[] args){
        circle(181.55f);
    }
    public static void circle(float radius){
        float pi = 3.14f;

        double area = pi*(Math.pow(radius, 2));
        double circum = 2*pi*radius;

        System.out.println("Area: " + area);
        System.out.println("Circumference: " + circum);

    }
}
