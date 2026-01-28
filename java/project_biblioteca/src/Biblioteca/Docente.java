package Biblioteca;

public class Docente extends Utente{


    private final int sconto = 20;

    public Docente(int id, String nome, String cognome) {
        super(id, nome, cognome);
    }

    @Override
    double calcolaSconto() {
        return 0;
    }

    public int getSconto() {
        return sconto;
    }


}
