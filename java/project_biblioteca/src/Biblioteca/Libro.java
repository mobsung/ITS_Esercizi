package Biblioteca;

public class Libro extends Pubblicazione{

    private int mora;

    public Libro(String codicePub, String titolo, String casaEditrice, int numCopie, double prezzoBase, int mora) {
        super(codicePub, titolo, casaEditrice, numCopie, prezzoBase);
        this.mora = mora;
    }

    @Override
    double calcolaPrezzo(int nGiorniRit) {
        return 0;
    }
}
