package Bosch;

import java.util.Scanner;

public class Exercicio6 {
    public static void  main(String[] args) {
        String num ;
        while (true){


            Scanner entrada = new Scanner(System.in);
            System.out.println("Digite um numero: ");
            num = entrada.nextLine();
            if(num.equalsIgnoreCase("sair")){
                break;
            }

            if( Integer.parseInt(num) == 0){
                System.out.println("nao da pra dividir por zero");
            }
            int aux = 0;

            for (int j = 1; j <= Integer.parseInt(num) ; j++) {
                if (Integer.parseInt(num) !=1){

                    if (Integer.parseInt(num)  % j == 0){
                        aux++;
                    }
                }

            }
            if(aux>2){
                System.out.println("nao é primo");
            }
            else{
                System.out.println(" e primo");
            }
        }
        
    
    }

}
