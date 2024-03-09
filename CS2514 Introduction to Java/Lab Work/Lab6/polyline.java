import java.util.List;
import java.util.ArrayList;

public class polyline{
    private List<Point> points = new ArrayList<Point>();
    public static void main(String[] args) {
        polyline m = new polyline();
        m.appendPoint(2, 4);
        m.appendPoint(4, 7);
        System.out.println(m.toString());
        System.out.println(m.getLength());
    }
    public polyline(List<Point> points1){
        points = points1;
    }

    public polyline(){

    }

    public void appendPoint(int x, int y){
        Point new_point = new Point(x, y);
        points.add(new_point);
    }

    public void appendPoint(Point e){
        points.add(e);
    }

    public String toString(){
        String output = "[";
        for (int i = 0; i < points.size(); i++){
            output += "(" + points.get(i).x + "," + points.get(i).y + ")";
        }
        output += "]";
        return output;
    }

    public double getLength(){
        double result = 0f;
        if (points.size() > 0) {
            for (int i = 1; i < points.size(); i++){
                Point prev_point = points.get(i-1);
                Point point = points.get(i);

                Double length = Math.sqrt(Math.pow(point.x - prev_point.x, 2) + 
                                            Math.pow(point.y - prev_point.y, 2));
                result += length;
            }
        }

        return result;
    } 
}

final class Point{
    public int x;
    public int y;
    public Point(int x1, int y1){
        x = x1;
        y = y1;
    }
}