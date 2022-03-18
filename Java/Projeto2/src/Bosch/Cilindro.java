package Bosch;

public class Cilindro {
    double altura;
    double raio;
    double volume;
    double superficial;
    double pi = 3.14;


    Cilindro(double altura, double raio){
        this.altura = altura;
        this.raio = raio;
    }
    double CalcularVolume(){
        volume = pi* (raio*raio)*altura;
        return volume;
    }
    double CalcularSuperficial() {
        superficial = (2*pi*raio*altura) + 2* (pi*(raio*raio));
        return superficial;
    }

}
