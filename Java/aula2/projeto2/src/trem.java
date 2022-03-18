public class trem {
    String name;
    double vel;
    double pos;

    public trem(String name, double pos, double vel) {
        this.name = name;
        this.vel = vel;
        this.pos = pos;
    }

    public void info() {
        System.out.println("--------------------------");
        System.out.println(this.name);
        System.out.println("Posicao:" + this.pos);
        System.out.println("Velocidade:" + this.vel + " Km/h");
        System.out.println("--------------------------");
    }

    public static double calculo(trem tremA, trem tremB) {
        double time = (tremA.pos - tremB.pos)/(tremB.vel- tremA.vel);
        double position = (tremA.pos+(tremA.vel * time));
        System.out.println(String.format("os trens se colidirao em %.2f horas  no km %.1f ",time,position));

        return 0;
    }


}
