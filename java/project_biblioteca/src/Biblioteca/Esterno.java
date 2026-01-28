package Biblioteca;

public class Esterno extends Utente{

    private boolean minorenne;

    public Esterno(int id, String nome, String cognome, boolean minorenne) {
        super(id, nome, cognome);
        this.minorenne = minorenne;
    }

    @Override
    double calcolaSconto() {
        return 0;
    }


}
