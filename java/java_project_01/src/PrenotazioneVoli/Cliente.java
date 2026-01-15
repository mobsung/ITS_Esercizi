package PrenotazioneVoli;

public class Cliente extends Thread{

    private final int numPosti;
    private final Assegnatore assegnatore;

    public Cliente(String nome, int numPosti, Assegnatore assegnatore) {
        super(nome);
        this.numPosti = numPosti;
        this.assegnatore = assegnatore;
    }

    public void run(){
        try {
            assegnatore.assegnaPosti(super.getName(), numPosti);
        } catch (PostiNonDispException e) {
            System.out.println(e);
        }
    }
}
