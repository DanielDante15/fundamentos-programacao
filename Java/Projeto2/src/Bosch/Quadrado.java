package Bosch;

public class Quadrado {
    double lado;
    double area;
    double perimetro;
    Quadrado(double lado){
        this.lado = lado;
    }
    double CaclularArea(){
        area = lado * lado;
        return area;
    }
    double CalcularPerimetro(){
        perimetro = lado * 4;
        return perimetro;
    }

}
