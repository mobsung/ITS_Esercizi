package Sconti;

import java.util.LinkedList;

public class Carrello {

    private LinkedList<Prodotto> prodotti = new LinkedList<>();

    public void addProdotto(Prodotto p){
        prodotti.add(p);
    }

    public double calcolaSpesa(Sconto s){
        double tot =
                prodotti.stream()
                        .map(p -> p.getQuantita() * p.getPrezzo())
                        .reduce((double) 0, (a, b) -> a + b);

        return tot * (1 - (s.getSconto() / 100.0));

    }
}
