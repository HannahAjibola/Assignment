import java.util.Scanner;

public class AscendingOrder{
	public static void main(String[]args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter first input:");
	float first = input.nextFloat();

	System.out.print("Enter second input:");
	float second = input.nextFloat();

	System.out.print("Enter third input:");
	float third = input.nextFloat();

	if(first > second && first > third){
		System.out.printf(%d%nfirst, second, third);
	}

	

	}

}
