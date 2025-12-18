package carrelloElettronico;

import java.util.Comparator;

public class ProdottoCompConsegna implements Comparator<Prodotto> {

    @Override
    public int compare(Prodotto p1, Prodotto p2){
        return Integer.compare(p1.getGiorniSpedizione(), p2.getGiorniSpedizione());
    }
}
