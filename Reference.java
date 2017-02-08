import java.util.*;
import java.math.*;

public class Reference
{
  public static void main(String[] args)
  {
    Scanner scan = new Scanner(System.in);
		BigInteger n = new BigInteger(scan.nextLine());
		BigInteger two = new BigInteger("2");
		BigInteger three = new BigInteger("3");
		BigInteger neg = new BigInteger("-1");
		if(!n.remainder(two).equals(BigInteger.ZERO)){
			if (n.equals(three)) {
				System.out.println(-2);
			}
			else{
				if(n.remainder(two).equals(BigInteger.ZERO))
					System.out.println(n.add(BigInteger.ONE).divide(two));
				else
					System.out.println(n.add(BigInteger.ONE).divide(two).multiply(neg));

			}
		}
		else{
			System.out.println(n.divide(two));
		}

  }
}
