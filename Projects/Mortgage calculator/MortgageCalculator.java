import java.util.Scanner;
import java.lang.Math;


    public class MortgageCalculator{

	
	

public static void main(String...args){
	Scanner userInput = new Scanner (System.in);
	
	    System.out.print("Welcome!");

  	    System.out.print("\nEnter the principal amount: ");
	double principal = userInput.nextDouble();

	    System.out.print("\nEnter the Annual interest rate: ");
	double annualInterestRate = userInput.nextDouble();

	    System.out.print("\nEnter the duration in years: ");
	double duration = userInput.nextDouble();

	
	double result = mortgage(principal, annualInterestRate, duration);

	    System.out.printf("Your monthly payment is $%.2f",  result);


}


	
	public static double mortgage(double principal, double annualInterestRate, double duration){
 
	    final double percent = 100;
	    final double months = 12;

	   double monthlyInterestRate = (annualInterestRate/percent)/months;
	   double durationInMonths = duration*months;
       	   double onePlusRate = 1 + monthlyInterestRate;
   
	   double numeratorCalculation = monthlyInterestRate*(Math.pow(onePlusRate,durationInMonths));

	   double denominatorCalculation = (Math.pow(onePlusRate,durationInMonths)) -1;

	   double monthlyPayment = principal*(numeratorCalculation / denominatorCalculation);

	   return monthlyPayment;


	}





	
    }
