package Biblioteca;

import java.util.Objects;

public class Tessera {

    private String codice;
    private double importo;

    public Tessera(String codice, double importo) {
        this.codice = codice;
        this.importo = importo;
    }

    public String getCodice() {
        return codice;
    }

    public double getImporto() {
        return importo;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Tessera tessera = (Tessera) o;
        return Objects.equals(codice, tessera.codice);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(codice);
    }

    void ricarica(double importo){

    }

    void scala(double importo){

    }

}
