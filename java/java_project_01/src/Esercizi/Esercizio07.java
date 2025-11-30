package Esercizi;

import java.util.Scanner;

public class Esercizio07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Esercizio n. 7
//		Letti dalla tastiera 2 numeri g e m, che rappresentino il giorno g del mese m, calcolare e stampare il numero di giorni trascorsi 
//		dall’inizio dell’anno (assumiamo di NON essere in un anno bisestile)
//		Esempio: ricevo in input 1 e 2 (cioè il primo di febbraio), allora l’output deve essere “dall’inizio dell’anno sono trascorsi 
//		31 giorni” (quindi il giorno stesso non si conta)
//		Casi particolari: 
//		    • inserendo 1, 1 devo avere “dall’inizio dell’anno sono trascorsi 0 giorni”
//		    • inserendo 31, 12 devo avere “dall’inizio dell’anno sono trascorsi 364 giorni”
//		    • inserendo una coppia g, m che non corrisponde ad una data reale, si riceve un messaggio d’errore “valori giorno/mese non coerenti”

		Scanner sc = new Scanner(System.in);

		System.out.println("Inserisci un numero n");
		int g = sc.nextInt();
		int m = sc.nextInt();

		String err = "valori giorno/mese non coerenti";

		int giorni = 0;
		
		if (m < 1 | m > 12) {
			System.out.println(err);
		} else {
			for (int i = 1; i <= m; i++) {

				switch (i) {
				case 1, 3, 5, 7, 8, 10, 12:
					if (i == m && (g < 1 || g > 31)) {
						System.out.println(err);
					} else {
						if (i < m) {
							giorni += 31;
						} else {
							giorni += g;
						}
						break;
					}
				case 2:
					if (i == m && (g < 1 || g > 28)) {
						System.out.println(err);
					} else {
						if (i < m) {
							giorni += 28;
						} else {
							giorni += g;
						}
						break;
					}
				case 4, 6, 9, 11:
					if (i == m && (g < 1 || g > 30)) {
						System.out.println(err);
					} else {
						if (i < m) {
							giorni += 30;
						} else {
							giorni += g;
						}
						break;
					}
				}

				System.out.println(giorni);

				sc.close();

			}
		}
	}

}
