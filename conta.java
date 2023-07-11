import java.util.Locale;
import java.util.Scanner;

public class conta {
    
	public static void main(String[] args) {

        Scanner scanner  = new Scanner(System.in).useLocale(Locale.US);

		System.out.println("Por favor digite o número da agência:");
        String Numero_Agencia = scanner.next();

        System.out.println("Digite o número da conta:");
        int Numero_Conta = scanner.nextInt();

        System.out.println("Digite seu nome:");
        String Nome_Cliente = scanner.next();

        System.out.println("Digite o saldo:");
        double Saldo = scanner.nextDouble();
		
		System.out.println( "Ola " +  Nome_Cliente + ", obrigado por criar uma conta em nosso banco, sua agencia é " +  Numero_Agencia + ", sua conta é "  +  Numero_Conta +  ", seu saldo é de R$ " +   Saldo + " e já está disponível na conta" );
		

    }
}


