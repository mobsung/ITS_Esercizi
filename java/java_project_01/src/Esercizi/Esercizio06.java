package Esercizi;

import java.util.Scanner;

public class Esercizio06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Esercizio n. 6
//		Letto dalla tastiera un numero intero n > 0, eseguire la scomposizione in fattori primi, stampando tutti i divisori.
//		Esempio: inserito 12, la scomposizione sarebbe 22 * 3, cioè 4*3.
//		Il programma deve stampare 2*2*3
//		Se il numero fosse primo, il programma avvisa con la stampa “il numero è primo”

		Scanner sc = new Scanner(System.in);

		System.out.println("Inserisci un numero n");
		int n = sc.nextInt();

		String out = "";

		if (n == 2) {
			System.out.println("Il numero è primo");
		}

		int i = 2;
		int m = n;

		while (i <= (int) (Math.sqrt(m))) {
			if (n % i == 0) {
				n /= i;
				out += ("*" + i);
			} else {
				i += 1;
			}
		}

		if (out.length() == 0) {
			System.out.println("Il numero è primo");
		} else {
			System.out.println(out);
		}
		sc.close();
	}

}
