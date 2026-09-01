import java.util.Scanner;
public class test {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// basic input output java program
		// System.out.println("Hello, World!");
		
		// System.out.print("Enter your name: ");
		// String name = sc.nextLine();
		// System.out.println("Hello, " + name + "!");


		// sc.close();
		// print all the even no. 

		// int i=s+1;
		System.out.println("enter the starting no.");
		int s=sc.nextInt();
		System.out.println("enter the end no.");

		int e=sc.nextInt();
		if(s%2==0) s+=2;
		else s+=1;
		
		for(int i=s;i<e;i+=2){
			System.out.println(i);
		}

		sc.close();
	}
}



//fragment in uml diagram alt(if else)
// using guards in UML diagrams