package viva;

// pacote para uso da API JDBC
import java.sql.*;

import javax.swing.JOptionPane;

public class PrincipalBanco {
	// String que compreende onde o banco esta
	static String URL = "jdbc:mysql://localhost:3306/meuBanco";
	// Login
	static String usuario = "root";
	// Senha
	static String senha = "root";
	public static void main(String [] args){
		try {
			// Carregando o Driver
			Class.forName("com.mysql.jdbc.Driver");
			// Efetuando a Conexao
			Connection conexao = DriverManager.getConnection(URL, usuario, senha);
			/* A partir daqui, voc� pode utilizar
			 * os statements para consultas ou insercoes... 
			 *
			*/
			// Sucesso na Conexao
			JOptionPane.showMessageDialog(null, "Sucesso na Conexao!");
			// Fechar Conexao
			conexao.close();
		} catch (ClassNotFoundException objErroDriver) {
			JOptionPane.showMessageDialog(null, "Erro no Driver");
		}
		catch (SQLException objErroConexao) {
			JOptionPane.showMessageDialog(null, "Erro na Conexao");
		}
	}
	
}
