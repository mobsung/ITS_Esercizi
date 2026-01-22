package Biblioteca;

import java.time.LocalDate;


public class Prestito {

    private LocalDate dataInizio;
    private LocalDate dataFine;
    private Pubblicazione pubblicazione;
    private Double prezzoFinale;

    public Prestito(LocalDate dataInizio, LocalDate dataFine, Pubblicazione pubblicazione) {
        this.dataInizio = dataInizio;
        this.dataFine = dataFine;
        this.pubblicazione = pubblicazione;
    }

    int getGiorniPrestati(){

    }
}
