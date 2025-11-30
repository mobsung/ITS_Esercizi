package EserciziClassi;

import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
	public static void main(String[] args) {
		
		/*
		 * Realizzare una classe col main nella quale si estrae randomicamente un numero
		 * tra 1 e 10 e l’utente deve indovinarlo. L’utente inserisce il numero e il
		 * sistema gli risponde una di queste frasi: Troppo piccolo, riprova con un
		 * numero maggiore Troppo grande, riprova con un numero minore Esatto! Hai
		 * indovinato con N tentativi Il sistema infatti calcola e memorizza il numero
		 * di tentativi e lo stampa alla fine Note: per l’estrazione casuale usare
		 * java.util.Random
		 */
		
		Scanner sc = new Scanner(System.in);

        int tentativi = 5;
        
        int counter = 0;
        
        
        Random r = new Random();
        
        int numero = r.nextInt(1, 11);
        
        while (counter < tentativi) {
        	
        	System.out.println("Inserisci un numera tra 0 e 10 hai ancora " + (tentativi - counter) + " tentativi!");
        	
        	int tentativo = sc.nextInt();
        	
        	if (tentativo < numero) {
        		System.out.println("Troppo piccolo, riprova con un numero maggiore");
        	} else if (tentativo > numero){
        		System.out.println("Troppo grande, riprova con un numero minore");
        	} else {
        		System.out.println("Esatto! Hai indovinato con " + (counter + 1) + " tentativi");
        		break;
        	}
        	
        	counter += 1;
        	
        	if (counter == tentativi) {
        		System.out.println("Hai esaurito i tentativi!");
        	}
        	
        	
        	
        }
		
        sc.close();
		
	}
}
