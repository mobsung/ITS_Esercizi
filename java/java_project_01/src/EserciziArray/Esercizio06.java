package EserciziArray;

public class Esercizio06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
		 * Esercizio n. 6 - inversione array vers.2 Letto in input un array A di n
		 * numeri interi, invertire l’ordine degli elementi. NB: utilizzare il SOLO
		 * array iniziale. Esempio: se A è (10,27,13, 4), allora devo ottenere A
		 * (4,13,27,10) Al termine dell’elaborazione stampare l'array A.
		 */

		int[] A = { 1, 2, 3, 4, 5, 6 };

		for (int i = 0; i < A.length / 2; i++) {

			int temp = A[i];

			A[i] = A[A.length - 1 - i];
			A[A.length - 1 - i] = temp;
		}

		for (int i = 0; i < A.length; i++) {
			System.out.println(A[i]);
		}
	}

}
