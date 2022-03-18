package Bosch;

public class Triangulo {
    double base;
    double altura;
    double area;
    double perimetro;


    Triangulo(double base, double altura){
        this.base = base;
        this. altura = altura;
    }
    double CaclularArea(){
        area = (base * altura);
        return area;
    }
    double CalcularPerimetro(){
        perimetro = (base*2) * 3;
        return perimetro;
    }
}
