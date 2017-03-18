/*
	Sintese :
		Objetivo : Demonstrar o uso de Loops rotulados
		Entrada : /
		Saída : /
		Autor : f_Candido	fagner7777777@gmail.com		@fagner_candido

*/

class LoopRotulado{


	public static void main(String[] args){
		/* 
			Loop Externo, expressão rotulado
			
		*/
		loopExterno:
			for(int contador = 0; contador < 5; contador++){
				for(int auxiliar = 0; auxiliar < 5; auxiliar++){
					System.out.println("Auxiliar : "+auxiliar);
					System.out.println("Contador : "+contador);
					/*
						Aqui ocorre a mágica, as instruções break e continue
						fazem com que o loop seja reavalidado ou lido novamente
					*/
					//break loopExterno;
					continue loopExterno;
				}
			}
	}

}
