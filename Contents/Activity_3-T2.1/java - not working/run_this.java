import java.io.FileNotFoundException;
import java.io.FileReader;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {

        String fileName = "/home/johni/Projects/compiler-jflex-javacup-examples/OtherCalc/src/calc.l";  

        Parser parser = new Parser(new Lexer(new FileReader(fileName)));
        try {
            parser.parse();
        }       
        catch (Exception e) {
            System.out.println("Falha geral.");
        }
    }
}
