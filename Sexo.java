/*
	Síntese
		Objetivo : Manipular Enum
		Entrada :
		Saída : Prints do Enum
		Autor : f_Candido	<fagner7777777@gmail.com>	@fagner_candido
*/

// Declaração do Enum
public enum Sexo{
	M("Masculino"), F("Feminino");
	
	private String sexo;

	Sexo(String sexo){
		this.sexo = sexo;
	}

	public String getSexo(){return this.sexo;}

}

class Principal{

	public static void main(String []args){
		// Posicao ordinal do Enum
		System.out.println(Sexo.M.ordinal());
		// Valor do Enum
		System.out.println(Enum.valueOf(Sexo.class, "M"));

	}

}
