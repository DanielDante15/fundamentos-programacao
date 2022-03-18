package Bosch;

public class Esfera {
    double raio;
    double volume;
    double superficial;
    double pi = 3.14;

    Esfera(double raio){
        this.raio = raio;
    }
    double CalcularVolume(){
        volume = (4/3) * (pi*(Math.pow(raio,3)));
        return volume;
    }
    double CalcularSuperficial() {
        superficial = 4 * pi * (raio*raio);
        return superficial;
    }

}
