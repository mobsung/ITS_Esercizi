package Sconti;

public class TestSconti {
    static void main() {

        Prodotto p1 = new Prodotto("latte", 2.5);
        Prodotto p2 = new Prodotto("mele", 2,0.6);
        Prodotto p3 = new Prodotto("pere", 4, 2.5);
        Prodotto p4 = new Prodotto("pane", 3,5.5);
        Prodotto p5 = new Prodotto("succo", 2.5);
        Prodotto p6 = new Prodotto("noci", 10,0.5);

        Carrello c1 = new Carrello();

        Sconto blackFriday = new BlackFriday();
        Sconto invernale = new Invernale();
        Sconto estivo = new Estivo();

        c1.addProdotto(p1);
        c1.addProdotto(p2);
        c1.addProdotto(p3);
        c1.addProdotto(p4);
        c1.addProdotto(p5);
        c1.addProdotto(p6);

        System.out.println("sconto blackfriday");
        System.out.println(c1.calcolaSpesa(blackFriday));

        System.out.println("\nsconto invernale");
        System.out.println(c1.calcolaSpesa(invernale));

        System.out.println("\nsconto estivo");
        System.out.println(c1.calcolaSpesa(estivo));

    }
}
