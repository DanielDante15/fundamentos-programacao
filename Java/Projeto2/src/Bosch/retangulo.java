package Bosch;

public class retangulo {
    double base;
    double altura;
    double area;
    double perimetro;

    retangulo(double base,double altura){
     this.base = base;
     this.altura = altura;
    }
    double CaclularArea(){
        area = base * altura;
        return area;

    }
    double CalcularPerimetro(){
        perimetro = (base*2) + (altura*2);

        return perimetro;
    }
}
