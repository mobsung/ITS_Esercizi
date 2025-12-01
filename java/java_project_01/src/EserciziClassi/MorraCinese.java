package EserciziClassi;

import java.util.Random;
import java.util.Scanner;

public class MorraCinese {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random r = new Random();
		
		
		while (true) {
			
			int nRandom = r.nextInt(0, 3);
			System.out.println("Digita '0 -> sasso', '1 -> carta', '2 -> forbici'");
			int utente = sc.nextInt();
			
			switch (utente) {
			case 0:
				if (utente == 0 && nRandom == 1) {
					System.out.println("TU: sasso --|-- AI: carta\nHai perso");
				} else if (utente == 0 && nRandom == 2) {
					System.out.println("TU: sasso --|-- AI: forbici\nHai vinto");
				} else {
					System.out.println("TU: sasso --|-- AI: sasso\nPareggio");
				}
				break;
			case 1:
				if (utente == 1 && nRandom == 0) {
					System.out.println("TU: carta --|-- AI: sasso\nHai vinto");
				} else if (utente == 1 && nRandom == 2) {
					System.out.println("TU: carta --|-- AI: forbici\nHai perso");
				} else {
					System.out.println("TU: carta --|-- AI: carta\nPareggio");
				}
				break;
			case 2:
				if (utente == 2 && nRandom == 0) {
					System.out.println("TU: forbici --|-- AI: sasso\nHai perso");
				} else if (utente == 2 && nRandom == 1) {
					System.out.println("TU: forbici --|-- AI: carta\nHai vinto");
				} else {
					System.out.println("TU: forbici --|-- AI: forbici\nPareggio");
				}
				break;
			}
			
			System.out.println("Se vuoi continuare digita 'SI' altrimenti 'NO'");
			String scelta = sc.next();
			if (scelta.equalsIgnoreCase("no")) {
				break;
			}
			
		}
		sc.close();
	}
}
