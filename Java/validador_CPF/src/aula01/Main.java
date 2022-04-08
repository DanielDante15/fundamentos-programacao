package aula01;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String cpf;
        int soma;
        String[] cpfDigitado;
        System.out.println("Validador de CPF");
        cpf = entrada.nextLine();
        cpfDigitado = cpf.split("");
        System.out.println(Arrays.toString(cpfDigitado));

        for (String digito:cpfDigitado) {



        }





    }
}
