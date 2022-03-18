package Bosch;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] figurasPlanas = {"Quadrado","Circulo","Triângulo","Hexágono","Retangulo"};
        String[] figurasEspaciais = {"Cubo","Esfera","Cilindro","Cone","Paralelepípedo","Piramide"};
        System.out.println("Calculo de Formas");
        Scanner entrada = new Scanner(System.in);

        while(true) {
            System.out.println("Digite a figura que deseja calcular:    [Plana/Espacial]");
            String tipo = entrada.nextLine();
            if(tipo.equalsIgnoreCase("plana")) {

                while (true) {
                    System.out.println("Digite a figura que deseja calcular: ");
                    String figura = entrada.nextLine();

                    if (figura.equalsIgnoreCase("quadrado")) {

                        while (true) {
                            System.out.println("Digite o lado do " + figura + ":");
                            String num = entrada.nextLine();
                            if (num.equalsIgnoreCase("sair")) {
                                break;
                            } else {
                                Quadrado q = new Quadrado(Double.parseDouble(num));
                                System.out.println("A área do " + figura + " é de: " + q.CaclularArea());
                                System.out.println("O perímetro do " + figura + " é de: " + q.CalcularPerimetro());
                            }
                        }
                    } else if (figura.equalsIgnoreCase("circulo")) {
                        while (true) {
                            System.out.println("Digite o raio do " + figura + ":");
                            String num = entrada.nextLine();
                            if (num.equalsIgnoreCase("sair")) {
                                break;
                            } else {
                                Circulo C = new Circulo(Double.parseDouble(num));
                                System.out.println("A área do " + figura + " é de: " + C.CaclularArea());
                                System.out.println("O perímetro do " + figura + " é de: " + C.CalcularPerimetro());
                            }
                        }
                    } else if (figura.equalsIgnoreCase("triangulo")) {
                        while (true) {
                            System.out.println("Digite a base: ");
                            String b = entrada.nextLine();
                            System.out.println("Digite a altura: ");
                            String h = entrada.nextLine();
                            if ((b.equalsIgnoreCase("sair")) || (b.equalsIgnoreCase("sair"))) {
                                break;
                            } else {
                                Triangulo t = new Triangulo(Double.parseDouble(b), (Double.parseDouble(h)));
                                System.out.println("A área do " + figura + " é de: " + t.CaclularArea());
                                System.out.println("O perímetro do " + figura + " é de: " + t.CalcularPerimetro());
                            }
                        }
                    } else if (figura.equalsIgnoreCase("hexagono")) {
                        while (true) {
                            System.out.println("Digite o lado do " + figura + ":");
                            String num = entrada.nextLine();
                            if (num.equalsIgnoreCase("sair")) {
                                break;
                            } else {
                                Hexagono C = new Hexagono(Double.parseDouble(num));
                                System.out.println("A área do " + figura + " é de: " + C.CaclularArea());
                                System.out.println("O perímetro do " + figura + " é de: " + C.CalcularPerimetro());
                            }
                        }
                    } else if (figura.equalsIgnoreCase("retangulo")) {
                        while (true) {
                            System.out.println("Digite a base: ");
                            String b = entrada.nextLine();
                            if ((b.equalsIgnoreCase("sair")) || (b.equalsIgnoreCase("sair"))) {
                                break;
                            }
                            System.out.println("Digite a altura: ");
                            String h = entrada.nextLine();
                            if ((b.equalsIgnoreCase("sair")) || (b.equalsIgnoreCase("sair"))) {
                                break;
                            } else {
                                retangulo t = new retangulo(Double.parseDouble(b), (Double.parseDouble(h)));
                                System.out.println("A área do " + figura + " é de: " + t.CaclularArea());
                                System.out.println("O perímetro do " + figura + " é de: " + t.CalcularPerimetro());
                            }
                        }
                    }
                    else if(figura.equalsIgnoreCase("sair")){
                        break;
                    }
                    else{

                        System.out.println("A figura que digitou é invalida");
                    }
                }
            }
            else if(tipo.equalsIgnoreCase("espacial")){
                System.out.println("Digite a figura que deseja calcular: ");
                String figura = entrada.nextLine();

                if(figura.equalsIgnoreCase("cubo")){
                    while (true) {
                        System.out.println("Digite a aresta do " + figura + ":");
                        String num = entrada.nextLine();
                        if (num.equalsIgnoreCase("sair")) {
                            break;
                        } else {
                            Cubo q = new Cubo(Double.parseDouble(num));
                            System.out.println("O volume do " + figura + " é de: " + q.CalcularVolume());
                            System.out.println("A área superficial do " + figura + " é de: " + q.CalcularSuperficial());
                        }
                    }
                }
                else if(figura.equalsIgnoreCase("esfera")){
                    while(true){
                        System.out.println("Digite o raio do " + figura + ":");
                        String num = entrada.nextLine();
                        if (num.equalsIgnoreCase("sair")) {
                            break;
                        } else {
                            Esfera q = new Esfera(Double.parseDouble(num));
                            System.out.println("O volume do " + figura + " é de: " + q.CalcularVolume());
                            System.out.println("A área superficial do " + figura + " é de: " + q.CalcularSuperficial());
                        }
                    }
                }
                else if(figura.equalsIgnoreCase("cilindro")){
                    while(true){
                        System.out.println("Digite a altura da " + figura + ":");
                        String altura = entrada.nextLine();
                        if (altura.equalsIgnoreCase("sair")) {
                            break;
                        }
                        System.out.println("Digite o raio da " + figura + ":");
                        String raio = entrada.nextLine();
                        if (raio.equalsIgnoreCase("sair")) {
                            break;
                        }
                        else {
                            Cilindro q = new Cilindro(Double.parseDouble(altura),Double.parseDouble(raio));
                            System.out.println("O volume do " + figura + " é de: " + q.CalcularVolume());
                            System.out.println("A área superficial do " + figura + " é de: " + q.CalcularSuperficial());
                        }
                    }

                }
            }
            else{
                System.out.println("O tipo que você digitou esta errado");
            }
        }
    }
}
