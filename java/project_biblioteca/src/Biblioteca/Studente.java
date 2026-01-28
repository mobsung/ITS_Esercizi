package Biblioteca;

public class Studente extends Utente{

    private boolean fuoriCorso;
    private final int sconto = 25;

    public Studente(int id, String nome, String cognome, boolean fuoriCorso) {
        super(id, nome, cognome);
        this.fuoriCorso = fuoriCorso;
    }

    @Override
    double calcolaSconto() {
        return 0;
    }

    public int getSconto() {
        return sconto;
    }

}
