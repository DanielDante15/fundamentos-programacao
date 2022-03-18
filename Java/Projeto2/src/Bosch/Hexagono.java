package Bosch;

public class Hexagono {
    double lado;
    double area;
    double perimetro;

    Hexagono(double lado){
        this.lado = lado;
    }
    double CaclularArea(){
        area = 3*(lado*lado)*Math.sqrt(3)/2;
        return area;

    }
    double CalcularPerimetro(){
        perimetro = 6*lado;

        return perimetro;
    }
}
