package EserciziArray;

public class Esercizio05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
		 * Esercizio n. 5 – stampa zigzag Letto in input un array A di n numeri interi,
		 * stampare gli elementi a zigzag, cioè il primo e l'ultimo, poi il secondo e il
		 * penultimo, e così via. NB: assumiamo la dimensione pari.
		 */

		int[] array = { 4, 6, 1, 4, 5, 7, 5, 3 };

		for (int i = array.length - 1; i > array.length / 2 - 1; i--) {

			System.out.print(array[array.length - 1 - i]);
			System.out.println(array[i]);

		}

	}

}
