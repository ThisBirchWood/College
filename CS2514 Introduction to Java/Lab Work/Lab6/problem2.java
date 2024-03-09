import java.util.Date;

public class problem2 {
    public static void main(String[] args) {
        Customer customer = new Customer("John");

        // Set customer as a premium member
        customer.setMember(true);
        customer.setMemberType("Premium");

        // Create a visit for the customer
        Visit visit = new Visit(customer.getName(), new Date());

        // Set expenses for services and products
        visit.setServiceExpense(100);
        visit.setProductExpense(50);

        // Display visit details
        System.out.println(visit.toString());
    }
}

class Customer {
    private String name;
    private boolean member = false;
    private String memberType = "";

    public Customer(String n){
        name = n;
    }

    public String getName(){
        return name;
    }

    public boolean isMember(){
        return member;
    }

    public void setMember(boolean m){
        member = m;
    }

    public String getMemberType(){
        return memberType;
    }

    public void setMemberType(String t){
        memberType = t;
    }

    public String toString(){
        return "Name: " + name + ", Type: " + memberType;
    }
}

class Visit{
    private Customer customer;
    private Date date;
    private double serviceExpense;
    private double productExpense;

    public Visit(String n, Date d){
        customer = new Customer(n);
        date = d;
    }

    public String getName(){
        return customer.getName();
    }

    public double getServiceExpense(){
        DiscountRate discounts = new DiscountRate();

        double discount = discounts.getServiceDiscountRate(customer.getMemberType());
        return serviceExpense - discount;
    }

    public void setServiceExpense(double ex){
        serviceExpense = ex;
    }

    public double getProductExpense(){
        DiscountRate discounts = new DiscountRate();

        double discount = discounts.getProductDiscountRate(customer.getMemberType());
        return productExpense - discount;
    }

    public void setProductExpense(double ex){
        productExpense = ex;
    }

    public double getTotalExpense(){
        return getServiceExpense() + getProductExpense();
    }

    public String toString(){
        return customer.getName() + " on " + date + " - Services: " + 
        getServiceExpense() + "$ - Product: " + getProductExpense() +
        "$ - Total: " + getTotalExpense() + "$.";
    }

}

class DiscountRate{
    double serviceDiscountPremium = 0.2;
    double serviceDiscountGold = 0.15;
    double serviceDiscountSilver = 0.1;
    double productDiscountPremium = 0.1;
    double productDiscountGold = 0.1;
    double productDiscountSilver = 0.1;

    public double getServiceDiscountRate(String type){
        if (type.equals("Premium")){
            return serviceDiscountPremium;
        } else if (type.equals("Gold")){
            return serviceDiscountGold;
        } else if (type.equals("Silver")){
            return serviceDiscountSilver;
        } else {
            return 0;
        }
    }

    public double getProductDiscountRate(String type){
        if (type.equals("Premium")){
            return productDiscountPremium;
        } else if (type.equals("Gold")){
            return productDiscountGold;
        } else if (type.equals("Silver")){
            return productDiscountSilver;
        } else {
            return 0;
        }
    }
}
