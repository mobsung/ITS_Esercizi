package Sconti;

public class Prodotto {

    private String nome;
    private int quantita;
    private double prezzo;

    public Prodotto(String nome, double prezzo) {
        this.nome = nome;
        this.quantita = 1;
        this.prezzo = prezzo;
    }

    public Prodotto(String nome, int quantita, double prezzo) {
        this.nome = nome;
        this.quantita = quantita;
        this.prezzo = prezzo;
    }

    public String getNome() {
        return nome;
    }

    public int getQuantita() {
        return quantita;
    }

    public double getPrezzo() {
        return prezzo;
    }


}
