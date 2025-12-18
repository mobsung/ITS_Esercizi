package carrelloElettronico;


import java.util.HashSet;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.TreeSet;

public class Carrello {

    private final HashSet<Prodotto> prodotti = new HashSet<>();


    @Override
    public String toString() {
        String prod = "";

        for (Prodotto p : prodotti){
            prod += p.toString() + "\n";
        }

        return prod;
    }

    public void aggiungi(Prodotto p) throws IdDuplicatoException{
        if (prodotti.add(p)){
            prodotti.add(p);
        } else {
            throw new IdDuplicatoException("Id è già presente");
        }
    }

    public void rimuovi(Prodotto p) throws IdNonPresenteException{
        if (prodotti.remove(p)){
            prodotti.remove(p);
        } else {
            throw new IdNonPresenteException("Id non presente");
        }
    }

    public double calcolaPrezzoTotale(){

        double totale = 0;

        for (Prodotto p : prodotti){
            totale += p.getPrezzo();
        }
        return totale;
    }

    public LinkedList<Prodotto> ordinaArticoliPrezzo(){

        TreeSet<Prodotto> orderedTree = new TreeSet<>(new ProdottoCompPrezzo());
        orderedTree.addAll(prodotti);

        return new LinkedList<>(orderedTree);
    }

    public LinkedList<Prodotto> ordinaArticoliConsegna(){

        TreeSet<Prodotto> orderedTree = new TreeSet<>(new ProdottoCompConsegna());
        orderedTree.addAll(prodotti);

        return new LinkedList<>(orderedTree);
    }

    public Prodotto articoloPiuCaro() throws NoSuchElementException {
        if (!this.ordinaArticoliPrezzo().isEmpty()){
            return this.ordinaArticoliPrezzo().getLast();
        } else {
            throw new NoSuchElementException("Il carrello è vuoto");
        }
    }

    public Prodotto articoloMenoCaro() throws NoSuchElementException {
        if (!this.ordinaArticoliPrezzo().isEmpty()){
            return this.ordinaArticoliPrezzo().getFirst();
        } else {
            throw new NoSuchElementException("Il carrello è vuoto");
        }
    }
}
