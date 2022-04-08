package Bosch;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String[] Cpf;
        int[] CpfInt = new int[11];
        int soma = 0;
        while (true){
            System.out.print("Digite o seu CPF: ");
            String cpfDigitado = entrada.nextLine();
            Cpf = cpfDigitado.replace(".", "").split("");
            if(cpfDigitado.equalsIgnoreCase("sair")) {
                System.out.println("Até mais!!");
                break;
            }
            if (Cpf.length != 9){
                System.out.println("O CPF que você digitou está incorreto!");
            }
            else {
                System.out.println("Os números que você inseriu são: "+Arrays.toString(Cpf));
                int aux = 0;
                int cont = 11;
                for (int i = 0; i < Cpf.length; i++) {
                    CpfInt[i] = Integer.parseInt(Cpf[i]);
                    cont -= 1;
                    aux = CpfInt[i] * cont;
                    soma += aux;
                }
                int D1 = 11 - (soma % 11);
                if (D1 > 9) {
                    D1 = 0;
                }
                CpfInt[9] = D1;
                aux = 0;
                soma = 0;
                cont = 11;
                for (int i = 0; i < 11; i++) {
                    aux = CpfInt[i] * cont;
                    cont -= 1;
                    soma += aux;
                }
                int D2 = 11 - (soma % 11);
                if (D2 > 9) {
                    D2 = 0;
                }
                CpfInt[10] = D2;
                System.out.println("O CPF gerado é: "+Arrays.toString(CpfInt));
            }
        }
    }
}
