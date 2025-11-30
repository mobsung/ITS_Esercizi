package EserciziArray;

import java.util.Scanner;

public class Esercizio09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Esercizio n. 9 – gioco lotto Realizzare il gioco del lotto su una sola ruota.
		 * Creare un array di dimensione 5 per la ruota ed estrarre randomicamente 5
		 * numeri compresi tra 1 e 90. Poi creare un secondo array per la giocata del
		 * giocatore: la dimensione sarà scelta dinamicamente (tra 1 e 5),poi il
		 * giocatore digita i numeri che vuole giocare (tutti diversi e compresi tra 1 e
		 * 90) Infine il sistema riporterà quanti numeri sono stati indovinati NB:
		 * Utilizzare (int)(Math.random()*90)
		 */

		int[] lotto = new int[5];
		int[] giocatore = new int[5];
		int valido = 0;

		Scanner sc = new Scanner(System.in);

		for (int i = 0; i < lotto.length; i++) {
			lotto[i] = (int) (Math.random() * 90);
		}

		System.out.println("Inserisci 5 numeri interi tra (0 e 90):");



		while (valido < giocatore.length) {

			int n = sc.nextInt();
			if (n >= 0 && n <= 90) {
				giocatore[valido] = n;
				valido += 1;

			} else {
				System.out.println("Inserisci un numero valido tra (0 e 90)");
			}

		}

		for (int i = 0; i < giocatore.length; i++) {
			
			
			System.out.print(lotto[i]+" ");
		}
		
		System.out.println();
		
		for (int num: lotto) {
			for (int snum: giocatore) {
				if (num == snum) {
					System.out.println("Numero " + num + " è stato indovinato");
				}
			}
			
		}
		
		sc.close();
	}

}
