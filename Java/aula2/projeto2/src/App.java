import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        while (true) {

            double velocidadeA, velocidadeB;
            String nameA = "Trem A", nameB = "Trem B";

            System.out.println("Colisao de trens");
            Scanner entrada = new Scanner(System.in);

            System.out.println("Digite a posicao do trem A:");
            double posicaoA = entrada.nextDouble();
            entrada.nextLine();
            System.out.println("Digite a posicao do trem B:");
            double posicaoB = entrada.nextDouble();
            entrada.nextLine();

            if (posicaoA > posicaoB) {
                System.out.println("Os trens nao vao colidir, tente novamente! ");
            } else {

                while (true) {

                    System.out.println("Digite a velocidade do trem A:");
                    velocidadeA = entrada.nextDouble();
                    entrada.nextLine();
                    if (velocidadeA > 300) {
                        System.out.println("O numero que voce digitou e invalido");

                    } else {
                        break;
                    }
                }

                while (true) {
                    System.out.println("Digite a velocidade do trem B:");
                    velocidadeB = entrada.nextDouble();
                    entrada.nextLine();

                    if (velocidadeB > 300) {
                        System.out.println("O numero que voce digitou e invalido");

                    } else {
                        break;
                    }
                }

                velocidadeB = velocidadeB * (-1);

                trem tremA = new trem(nameA, posicaoA, velocidadeA);
                trem tremB = new trem(nameB, posicaoB, velocidadeB);

                tremA.info();
                tremB.info();
                trem.calculo(tremA,tremB);

            }
        }
    }

}
