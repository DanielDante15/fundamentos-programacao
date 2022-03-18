package Bosch;

public class Cubo {
    double aresta;
    double volume;
    double superficial;
    double pi = 3.14;
    Cubo(double aresta){
        this.aresta = aresta;

    }
    double CalcularVolume(){
        volume = (Math.pow(aresta,3));
        return volume;
    }
    double CalcularSuperficial() {
        superficial = (aresta*aresta)* 6;
        return superficial;
    }
}
