public class problem3 {
    public static void main(String[] args) {
        Cylinder c = new Cylinder(4, 3, "blue");
        System.out.println(c.getVolume());
        c.setHeight(5);
        System.out.println(c.getVolume());
        System.out.println(c.getArea());
        System.out.println(c.toString());

        Circle myCircle = new Circle();
        myCircle.setRadius(3);
        System.out.println(myCircle.getArea());
        System.out.println(myCircle.getColor());
    }
}

class Circle{
    private double radius = 1.0;
    private String color = "red";

    public Circle(){
    }

    public Circle(double r){
        this.radius = r;
    }

    public Circle(double r, String c){
        this.radius = r;
        this.color = c;
    }

    public double getRadius(){
        return this.radius;
    }

    public void setRadius(double r){
        this.radius = r;
    }

    public String getColor(){
        return this.color;
    }

    public void setColor(String c){
        this.color = c;
    }

    public double getArea(){
        return Math.PI*Math.pow(this.radius, 2);
    }

    public String toString(){
        return "Circle[radius-" + this.radius + ",color-" + this.color + "]";
    }
}

class Cylinder extends Circle{
    private double height = 1.0;

    public Cylinder(){
        super();
    }

    public Cylinder(double r){
        super(r);
    }

    public Cylinder(double r, double h){
        super(r);
        this.height = h;
    }

    public Cylinder(double r, double h, String c){
        super(r, c);
        this.height = h;
    }

    public double getHeight(){
        return this.height;
    }

    public void setHeight(double h){
        this.height = h;
    }

    public double getVolume(){
        return Math.PI * Math.pow(getRadius(), 2) * this.height;
    }

    @Override
    public double getArea(){
        return (2*Math.PI * getRadius() * getHeight()) + (2*Math.PI * Math.pow(getRadius(), 2));
    }

    @Override
    public String toString(){
        return "Circle[radius-" + getRadius() + ",height-" + getHeight() + ",color-" + getColor() + "]"; 
    }

}