package Biblioteca;

import java.util.LinkedList;
import java.util.Objects;

public abstract class Utente {

    private int id;
    private String nome;
    private String cognome;
    private Tessera tessera;
    private LinkedList<Prestito> prestiti = new LinkedList<>();

    public Utente(int id, String nome, String cognome) {
        this.id = id;
        this.nome = nome;
        this.cognome = cognome;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getCognome() {
        return cognome;
    }

    public Tessera getTessera() {
        return tessera;
    }

    void setTessera(Tessera t){
        tessera = t;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Utente utente = (Utente) o;
        return id == utente.id;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(id);
    }

    void aperturaPrestito(Pubblicazione p){

    }

    Prestito getPrestito(String codicePub){
        return prestiti.get(1);
    }

    abstract double calcolaSconto();
}

