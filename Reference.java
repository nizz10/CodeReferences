/* A problem from codeforces:
For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 1015).

Output
Print f(n) in a single line.
*/


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
