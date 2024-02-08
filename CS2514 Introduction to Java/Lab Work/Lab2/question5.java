public class question5 {
    public static void main(String[] args){
        loan_category(1500); // alice
        loan_category(700); // bob
        loan_category(100); // clive
    }

    public static void loan_category(int earnings){
        int category;
        double loan_amount;
        if (earnings >= 1000){
            category = 1;
        } else if (earnings >= 500 && earnings < 1000){
            category = 2;
        } else if (earnings >= 200 && earnings < 500){
            category = 3;
        } else {
            category = 4;
        }

        switch(category){
            case 1:
                loan_amount = earnings * 3.5;
                break;
            case 2:
                loan_amount = earnings * 2.5;
                break;
            case 3:
                loan_amount = earnings * 2;
                break;
            default:
                loan_amount = 0;
                break;
        }

        System.out.println("Loan amount: " + loan_amount + " and category: " + category);

    }
}
