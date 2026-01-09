package OperazioniProdotto;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class testOperazioni {
    static void main() {

        ArrayList<Prodotto> catalogo = new ArrayList<Prodotto>();
        catalogo.add(new Prodotto(133, "latte", "alimentare", 100, true, 2.5, 0));
        catalogo.add(new Prodotto(134, "latte UHT", "alimentare", 0, false, 2.5, 0));
        catalogo.add(new Prodotto(113, "pomodori", "alimentare", 50, true, 1.5, 5));
        catalogo.add(new Prodotto(123, "libro", "media", 10, true, 10, 5));
        catalogo.add(new Prodotto(155, "maglietta", "abbigliamento", 20, true, 25, 10));
        catalogo.add(new Prodotto(184, "cd musicale", "media", 0, false, 12.5, 0));
        catalogo.add(new Prodotto(143, "smartphone", "elettronica", 80, true, 250, 10));
        catalogo.add(new Prodotto(144, "cuffie", "elettronica", 0, false, 250, 10));

        System.out.println("-->il numero di categorie");
        long numeroCategorie =
                catalogo.stream()
                        .map(p -> p.getCategoria())
                        .distinct()
                        .count();
        System.out.println(numeroCategorie);

        System.out.println("-->le categorie ordinate in ordine alfabetico, senza elementi doppi");
        List<String> categorieOrdinateUniche =
                catalogo.stream()
                        .map(p -> p.getCategoria())
                        .sorted()
                        .distinct()
                        .toList();
        categorieOrdinateUniche.forEach(c -> System.out.print(c + ", "));

        System.out.println("-->i nomi dei prodotti ordinati per prezzo crescente");
        List<String> nomiOrdinatiPerPrezzo =
                catalogo.stream()
                        .sorted((a, b) -> Double.compare(a.getPrezzo(), b.getPrezzo()))
                        .map(p -> p.getDescrizione())
                        .toList();
        nomiOrdinatiPerPrezzo.forEach(c -> System.out.print(c + ", "));

        System.out.println("-->i prodotti ordinati in base allo sconto");
        List<Prodotto> prodottiOrdinatiPerSconto =
                catalogo.stream()
                        .sorted((a, b) -> Integer.compare(a.getSconto(), b.getSconto()))
                        .toList();
        prodottiOrdinatiPerSconto.forEach(c -> System.out.print(c + ", "));

        System.out.println("-->il prodotto con lo sconto maggiore");
        Optional<Prodotto> prodottoScontoMaggiore =
                catalogo.stream()
                        .max((a, b) -> Integer.compare(b.getSconto(), a.getSconto()));
        System.out.println(prodottoScontoMaggiore);

        System.out.println("-->la somma dei prezzi dei prodotti alimentari");
        double sommaPrezzi =
                catalogo.stream()
                        .map((p) -> p.getPrezzo())
                        .reduce((double) 0, (a, b) -> a + b);
        System.out.println(sommaPrezzi);

        System.out.println("-->Un Optional vuoto a seguito di una ricerca di prodotto per una categoria inesistente (es. giocattoli)");
        Optional<Prodotto> prodottoInesistente =
                catalogo.stream()
                        .filter(p -> p.getDescrizione().equals("giocattoli"))
                        .findAny();
        System.out.println(prodottoInesistente);

        System.out.println("-->Il prodotto con prezzo più alto nella categoria media");
        Optional<Prodotto> prodottoPrezzoMaxMedia =
                catalogo.stream()
                        .filter(p -> p.getCategoria().equals("media"))
                        .max((a, b) -> Double.compare(b.getPrezzo(), a.getPrezzo()));
        System.out.println(prodottoPrezzoMaxMedia);

        System.out.println("-->I nomi dei prodotti non disponibili");
        List<String> prodottiNonDisponibili =
                catalogo.stream()
                        .filter(p -> !p.isDisponibile())
                        .map(p -> p.getDescrizione())
                        .toList();
        prodottiNonDisponibili.forEach(c -> System.out.print(c + ", "));

    }
}
