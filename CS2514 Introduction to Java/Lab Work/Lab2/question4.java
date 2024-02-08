public class question4 {
    public static void main(String[] args){
        results(new int[][]{{90, 60, 80}, {50, 0, 30}, {60, 70, 75}});
    }

    public static void results(int[][] scores){
        for (int i = 0; i < scores.length; i++){
            double average = 0;
            for (int j = 0; j < scores[i].length; j++){
                average += scores[i][j];
            }
            average = average/scores[i].length;
            System.out.println("Student " + (i+1) + ": " + end_result(average));
        }

    }

    private static String end_result(double score){
        if (score >= 80){
            return "A";
        } else if (score >= 60){
            return "B";
        } else if (score >= 40){
            return "C";
        } else {
            return "D";
        }
    }
}
