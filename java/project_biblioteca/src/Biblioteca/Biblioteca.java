package Biblioteca;

import java.util.HashMap;
import java.util.LinkedList;

public class Biblioteca {

    private String nome;
    private String localita;
    private final HashMap<Integer, Utente> utenti = new HashMap<>();
    private final HashMap<String, Pubblicazione> catalogo = new HashMap<>();

    public Biblioteca(String nome, String localita) {
        this.nome = nome;
        this.localita = localita;
    }

    void registraNuovoUtente(Utente ut){
        if (!utenti.containsValue(ut)){
            String tID = ut.getId()+": "+ut.getCognome()+" "+ut.getNome();
            Tessera t = new Tessera(tID, 100);
            ut.setTessera(t);
            utenti.put(ut.getId(), ut);

        }
    }

    void registraNuovaPubblicazione(Pubblicazione pub){
        if (!catalogo.containsValue(pub)){
            catalogo.put(pub.getCodicePub(), pub);
        }
    }

    void presta(String codicePub, int idUt){
        if (utenti.containsKey(idUt) && catalogo.containsKey(codicePub)){
            utenti.get(idUt).aperturaPrestito(catalogo.get(codicePub));
        }
    }
    void riconsegna(String codicePub, int idUt){

    }

    Utente getUtente(int idUt){
        return utenti.get(idUt);
    }

    Pubblicazione getPubblicazione(String codicePub){
        return catalogo.get(codicePub);
    }

}
