package EserciziArray;

public class Esercizio07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
		 * Esercizio n. 7 – elementi comuni Letti in input due array A e B, di lunghezza
		 * n ed m, stampare tutti gli elementi comuni ad A e B.
		 */

		int[] A = { 1, 4, 3, 4, 5, 6 };
		int[] B = { 4, 5, 6, 7, 8, 9 };

		for (int i = 0; i < A.length; i++) {

			for (int j = 0; j < B.length; j++) {

				if (A[i] == B[j]) {

					System.out.println(A[i]);

				}

			}

		}

	}

}
