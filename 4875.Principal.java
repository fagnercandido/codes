/*
	Sintese:
		Objetivo : Manipular arquivos CSV em Java
		Entrada : Um arquivo CSV
		Saida : Um arquivo CSV
		Autor : f_Candido - fagner7777777@gmail.com
*/

// Importacao da Lib OpenCSV
import au.com.bytecode.opencsv.CSVReader;
import au.com.bytecode.opencsv.CSVWriter;
// Importacao da propria API
import java.io.FileReader;
import java.io.IOException;
import java.io.StringWriter;
import java.util.List;

// Interface com o comportamento
interface ManipulacaoCSV{
	public static final String FILECSV="file.csv";
	public void readCSV() throws IOException ;
	public void writeCSV() throws IOException;
}

class CSVTests implements ManipulacaoCSV {
	
	private CSVReader fileRead;
	private StringWriter stringWriter;
	private CSVWriter fileWrite;
	private List<String[]> all;	

	// Le o arquivo CSV
	public void readCSV()throws IOException{
		this.fileRead = new CSVReader(new FileReader(FILECSV));
	}
	// Escreve no arquivo CSV
	public void writeCSV() throws IOException{
		stringWriter = new StringWriter();
		fileWrite = new CSVWriter(stringWriter);
		fileWrite.writeAll(all);
	}
	// Popula o Array
	public void fill() throws IOException{
		all = fileRead.readAll();
	}
}

// Main
public class Principal{
	public static void main(String[] args) throws IOException {
		CSVTests objTests = new CSVTests();
		objTests.readCSV();
		objTests.fill();
		objTests.writeCSV();
	}
}
