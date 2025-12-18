package carrelloElettronico;

public class TestCarrello {
    static void main() {

        Prodotto p1 = new Prodotto("#1", "marcaTest1", "modelloTest1", 10.21, 1);
        Prodotto p2 = new Prodotto("#2", "marcaTest2", "modelloTest2", 1.21, 2);
        Prodotto p3 = new Prodotto("#3", "marcaTest3", "modelloTest3", 7.2, 7);
        Prodotto p4 = new Prodotto("#4", "marcaTest4", "modelloTest4", 22.21, 11);
        Prodotto p5 = new Prodotto("#5", "marcaTest5", "modelloTest5", 3.11, 1);

        Carrello c1 = new Carrello();

        System.out.println(c1);

        c1.aggiungi(p1);
        c1.aggiungi(p2);
        c1.aggiungi(p3);
        c1.aggiungi(p4);
        c1.aggiungi(p5);

        System.out.println(c1);

        System.out.println("Articolo meno caro:");
        System.out.println(c1.articoloMenoCaro() + "\n");

        System.out.println("Articolo più caro");
        System.out.println(c1.articoloPiuCaro() + "\n");

        System.out.println("Prezzo totale");
        System.out.println(c1.calcolaPrezzoTotale() + "\n");

        System.out.println("Ordinamento per giorni consegna");
        System.out.println(c1.ordinaArticoliConsegna() + "\n");

        System.out.println("Ordinamento per prezzo");
        System.out.println(c1.ordinaArticoliPrezzo() + "\n");


    }
}
