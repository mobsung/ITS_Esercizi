package Biblioteca;

public class Libro extends Pubblicazione{

    private int mora;

    public Libro(String codicePub, String titolo, String casaEditrice, int numCopie, double prezzoBase) {
        super(codicePub, titolo, casaEditrice, numCopie, prezzoBase);
    }

    @Override
    double calcolaPrezzo(int nGiorniRit) {

        double prezzoIniziale = getNumCopie() * getPrezzoBase();

        if (nGiorniRit <= 5) return prezzoIniziale;
        return prezzoIniziale * (1 + (double) ((nGiorniRit - 5) * 25) / 100);
    }
}
