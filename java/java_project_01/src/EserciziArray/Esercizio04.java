package EserciziArray;

public class Esercizio04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Creare un array A di n numeri interi e popolarlo dinamicamente. Calcolare e
		 * stampare: • la somma di tutti gli elementi • la somma degli elementi di posto
		 * pari (il posto zero viene contato nei pari!) • la somma degli elementi di
		 * posto dispari • la media aritmetica di tuti gli elementi
		 */

		int[] array = { 4, 6, 1, 4, 5, 7 };

		int pari = 0;
		int dispari = 0;

		for (int i = 0; i < array.length; i++) {

			if (i % 2 == 0) {
				pari += array[i];
			} else {
				dispari += array[i];
			}
		}


		System.out.println("totale numeri posizione pari: " + pari);
		System.out.println("totale numeri posizione dispari: " + dispari);
		System.out.println("totale numeri: " + (pari + dispari));
		System.out.println("media: " + ((double) (pari + dispari) / array.length));

	}

}
