public class problem4 {
    public static void main(String[] args) {
        test_square();
    }

    public static void test_shape(){
        Shape s = new Shape();
        System.out.println(s.getColor());
        System.out.println(s.isFilled());

        s.setColor("blue");
        s.setFilled(false);;
        System.out.println(s.getColor());
        System.out.println(s.isFilled());
    }

    public static void test_circle(){
        Circle c = new Circle();
        System.out.println(c.getColor());
        System.out.println(c.getRadius());
        
        c.setRadius(4);
        System.out.println(c.getRadius());
        System.out.println(c.getPerimeter());
        System.out.println(c.toString());
    }

    public static void test_rectangle(){
        Rectangle r = new Rectangle();
        System.out.println(r.toString());
        System.out.println(r.getArea());
        System.out.println(r.getPerimeter());

        r.setWidth(5);
        r.setLength(8);
        System.out.println(r.toString());
        System.out.println(r.getArea());
        System.out.println(r.getPerimeter());
    }

    public static void test_square(){
        Square s = new Square();
        System.out.println(s.toString());

        s.setSide(45);
        System.out.println(s.getPerimeter());
        System.out.println(s.toString());

        s.setLength(30);
        System.out.println(s.getArea());
        System.out.println(s.toString());
    }
}

class Shape{
    private String color;
    private boolean filled;

    public Shape(){
        this.color = "green";
        this.filled = true;
    }

    public Shape(String color, boolean filled){
        this.color = color;
        this.filled = filled;
    }

    public String getColor(){
        return this.color;
    }

    public void setColor(String color){
        this.color = color;
    }

    public boolean isFilled(){
        return this.filled;
    }

    public void setFilled(boolean filled){
        this.filled = filled;
    }

    public String toString(){
        String return_string = "A Shape with color of " + this.color;

        if (this.filled == true){
            return return_string + " and filled";
        } else {
            return return_string + " and not filled";
        }
    }
}

class Circle extends Shape{
    private double radius;

    public Circle(){
        super();
        this.radius = 1.0;
    }

    public Circle(double radius){
        super();
        this.radius = radius;
    }

    public Circle(double radius, String color, boolean filled){
        super(color, filled);
        this.radius = radius;
    }

    public double getRadius(){
        return this.radius;
    }

    public void setRadius(double radius){
        this.radius = radius;
    }

    public double getArea(){
        return Math.PI*Math.pow(this.radius, 2);
    }

    public double getPerimeter(){
        return 2*Math.PI*this.radius;
    }

    @Override
    public String toString(){
        return "A Circle with radius=" + this.radius + ", which is a subclass of " + super.toString();
    }
}

class Rectangle extends Shape{
    private double width;
    private double length;

    public Rectangle(){
        super();
        this.width = 1.0;
        this.length = 1.0;
    }

    public Rectangle(double width, double length){
        super();
        this.width = width;
        this.length = length;
    }

    public Rectangle(double width, double length, String color, boolean filled){
        super(color, filled);
        this.width = width;
        this.length = length;
    }

    public double getWidth(){
        return this.width;
    }

    public void setWidth(double width){
        this.width = width;
    }

    public double getLength(){
        return this.length;
    }

    public void setLength(double length){
        this.length = length;
    }

    public double getArea(){
        return this.length * this.width;
    }

    public double getPerimeter(){
        return (2*this.length) + (2*this.width);
    }

    @Override
    public String toString(){
        return "A Rectangle with width=" + this.width + " and length=" + this.length + ", which is a subclass of " + super.toString();
    }
}

class Square extends Rectangle{
    public Square(){
        super();
    }

    public Square(double side){
        super(side, side);
    }

    public Square(double side, String color, boolean filled){
        super(side, side, color, filled);
    }

    public double getSide(){
        return this.getLength();
    }

    public void setSide(double side){
        super.setLength(side);
        super.setWidth(side);
    }

    @Override
    public void setWidth(double width){
        this.setSide(width);
    }

    @Override
    public void setLength(double length){
        this.setSide(length);
    }
    
    @Override
    public String toString(){
        return "A Square which is a subclass of " + super.toString();
    }
}
