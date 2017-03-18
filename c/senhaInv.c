/*
	Autor : Fagner Candido
	E-mail : fagner7777777@gmail.com
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <termios.h>
#define MAX_SENHA 10 // Máximo para a Senha


int main(int argc, char **argv){
	// Declarações
	   /*Define as estrutura manipularão o terminal*/
	   struct termios antigoTermios, novoTermios;
	   char senha[MAX_SENHA];
	// Instruções
	   /*
	   	Função que obtém as informações do Terminal
	   	file(stdin) : Entrada Padrão
	   	antigoTermios : Recebe as informações
	   */
	   tcgetattr(fileno(stdin), &antigoTermios);
	   /*
	   	Atribuímos as características do terminal
	   	a estrutura
	   */
	   novoTermios = antigoTermios;
	   /*
	   	Definimos uma Propriedade : Terminal não irá imprimir nada
	   */
	   novoTermios.c_lflag &= ~ECHO;
	   printf("Informe a Senha : ");
	   /*
	   	Novas Características ao Terminal
	   */
	   if(tcsetattr(fileno(stdin), TCSAFLUSH, &novoTermios ) != 0 ){  /*Caso dê erro*/
        	printf("Erro!\n" );  
                exit(0);  
           }  
           else{  /*Caso dê Certo*/
        	fgets(senha, MAX_SENHA, stdin);
                tcsetattr(fileno(stdin), TCSANOW, &antigoTermios );  
           }  
           printf("\nSenha : %s", senha); 
	   return 0;

}
