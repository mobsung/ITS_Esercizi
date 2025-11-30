package EserciziClassi;

import java.util.Date;
import java.util.Scanner;

public class DifferenzaDate {
	public static void main(String[] args) {

		/*
		 * Scrivere una classe java con il metodo main che calcola quante ore e quanti
		 * minuti mancano alla fine della lezione
		 * 
		 * Versione 1: assumere che la lezione termina alle 18.00 
		 * Versione 2: consentire
		 * all’utente di inserire l’orario di uscita (acquisendo le ore e i minuti con 2
		 * letture separate)
		 * 
		 * Nota: utilizzare 2 oggetti di tipo java.util.Date
		 */

		Date fine = new java.util.Date(125, 10, 28, 19, 30);
		Date d = new Date();
		
		Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci ora e minuti:");

        int h = sc.nextInt();
        int m = sc.nextInt();
        
        d.setHours(h);
        d.setMinutes(m);
        
        int oreRimanenti = fine.getHours() - d.getHours();
        int minRimanenti = fine.getMinutes() - d.getMinutes();
        
        if (fine.getMinutes() - d.getMinutes() < 0) {
        	oreRimanenti -= 1;
        	minRimanenti = 60 + minRimanenti;
        }
        
        
        
        System.out.println("ORE rimanenti: "+oreRimanenti);
        System.out.println("MINUTI rimanenti: "+minRimanenti);
		
		sc.close();

	}
}
