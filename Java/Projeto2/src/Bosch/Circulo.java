package Bosch;


public class Circulo {
    double raio;
    double area;
    double perimetro;
    double pi = 3.14;
    Circulo(double raio){
        this.raio = raio;

    }

    double CaclularArea(){
        area =  pi * (raio*raio) ;
        return area;

    }
    double CalcularPerimetro(){
        perimetro = 2 * pi * raio;
        return perimetro;
    }
}
