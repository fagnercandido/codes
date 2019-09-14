import java.util.function.*;

public class Funcoes {

	public static void main(String ...args){
		Function<Integer, Integer> myFunction = (x) -> x*x + 2;
		System.out.println(myFunction.apply(5));
	}


}
