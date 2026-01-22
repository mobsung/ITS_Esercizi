package Biblioteca;

import java.util.Objects;

public class Pubblicazione {

    private String codicePub;
    private String titolo;
    private String casaEditrice;
    private int numCopie;
    private double prezzoBase;

    public Pubblicazione(String codicePub, String titolo, String casaEditrice, int numCopie, double prezzoBase) {
        this.codicePub = codicePub;
        this.titolo = titolo;
        this.casaEditrice = casaEditrice;
        this.numCopie = numCopie;
        this.prezzoBase = prezzoBase;
    }

    public String getCodicePub() {
        return codicePub;
    }

    public String getTitolo() {
        return titolo;
    }

    public String getCasaEditrice() {
        return casaEditrice;
    }

    public int getNumCopie() {
        return numCopie;
    }

    public double getPrezzoBase() {
        return prezzoBase;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Pubblicazione that = (Pubblicazione) o;
        return Objects.equals(codicePub, that.codicePub);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(codicePub);
    }


}
