package PrenotazioneVoli;

public class Assegnatore {

    private int postiDisponibili = 20;

    synchronized void assegnaPosti(String cliente, int numPosti) throws PostiNonDispException{
        if (postiDisponibili - numPosti >= 0){
            System.out.println("->Posti disponibili " + postiDisponibili);
            System.out.println(Thread.currentThread().getName() + ": Sto provando a prenotare " + numPosti + " biglietti.");
            System.out.println("Assegnazione avvenuta con successo per il cliente >" + cliente + "< Sono stati assegnati " + numPosti + " posti.\n");
            postiDisponibili -= numPosti;
        } else {
            throw new PostiNonDispException("Non ci sono abbastanza posti liberi per coprire " + numPosti + " posti per il cliente >" + cliente + "<\n");
        }
    }

    synchronized int getTotalePosti(){
        return postiDisponibili;
    }

}
