package carrelloElettronico;

import java.util.Objects;

public class Prodotto {

    private final String id;
    private String marca;
    private String modello;
    private double prezzo;
    private int giorniSpedizione;

    public Prodotto(String id, String marca, String modello, double prezzo,  int giorniSpedizione) {
        this.id = id;
        this.marca = marca;
        this.modello = modello;
        this.prezzo = prezzo;
        this.giorniSpedizione = giorniSpedizione;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public int getGiorniSpedizione() {
        return giorniSpedizione;
    }

    public String getModello() {
        return modello;
    }

    public String getMarca() {
        return marca;
    }

    public String getId() {
        return id;
    }

    @Override
    public String toString() {
        return "{" +
                "id='" + id + '\'' +
                ", marca='" + marca + '\'' +
                ", modello='" + modello + '\'' +
                ", prezzo=" + prezzo +
                ", giorniSpedizione=" + giorniSpedizione +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Prodotto prodotto = (Prodotto) o;
        return Objects.equals(id, prodotto.id);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(id);
    }
}
