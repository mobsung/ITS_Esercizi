package PrenotazioneVoli;

public class Simulazione {
    static void main() {

        Assegnatore as = new Assegnatore();

        Cliente c1 = new Cliente("Stefano", 4, as);
        Cliente c2 = new Cliente("Cristiano", 6, as);
        Cliente c3 = new Cliente("Dario", 5, as);
        Cliente c4 = new Cliente("Marcel", 7, as);

        c1.start();
        c2.start();
        c3.start();
        c4.start();

    }
}
