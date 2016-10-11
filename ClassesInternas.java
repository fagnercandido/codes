/*
	Sintese :
		Objetivo : Demonstrar o uso de Classes Internas
		Entrada : n/d
		Saída : n/d
		Autor :	Fagner Candido
			f_Candido	
			@fagner_candido
			fagner7777777@gmail.com
*/
class ExternalClass{

	private String name;

	public ExternalClass(){
		name = "Ronaldo";
	}

	public String getName(){
		return this.name;	
	}
	
	// Declaracao da classe interna
	// E um membro da classe ExternalClass
	class InnerClass{
		public void printArgs(){
			// Sendo membro, tem acesso aos membros da classe externa
			System.out.println("Argumento da Classe Externa : "+name);
			// Acesso atraves da ExternalClass
			System.out.println("Argumento da Classe Externa[Com Encapsulamento] : "+ExternalClass.this.getName());
			// Print da instancia
			// Aparece desta forma, por conta da sobrescricao de toString
			System.out.println("Classe Interna : "+this);
		}	
		// Sobrescrevendo toString
		public String toString(){
			return "InnerClass";
		}
	}

}

class Main{
	public static void main(String[] args){
		// Criando um instancia de InnerClass, uma sintaxe diferente		
		ExternalClass.InnerClass objInt = new ExternalClass().new InnerClass();
		objInt.printArgs();
		
	}
}
