package Biblioteca;

public class Rivista extends Pubblicazione{

    private int statoUsura;

    public Rivista(String codicePub, String titolo, String casaEditrice, int numCopie, double prezzoBase, int statoUsura) {
        super(codicePub, titolo, casaEditrice, numCopie, prezzoBase);
        this.statoUsura = statoUsura;
    }

    @Override
    double calcolaPrezzo(int nGiorniRit) {
        return getNumCopie() * (getPrezzoBase());
    }

}
