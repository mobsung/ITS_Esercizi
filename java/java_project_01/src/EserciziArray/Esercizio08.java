package EserciziArray;

public class Esercizio08 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Esercizio n. 8 – elementi diversi Letti in input due array A e B, di
		 * lunghezza n ed m, stampare tutti gli elementi presenti in B, ma non in A.
		 */

		int[] A = { 1, 4, 7, 4, 5 };
		int[] B = { 4, 5, 6, 7, 8, 9 };
		

		for (int i = 0; i < B.length; i++) {

			boolean exists = false;
			
			for (int j = 0; j < A.length; j++) {

				if (B[i] == A[j]) {

					exists = true;
					break;

				}

			}
			
			if(!exists) {
				System.out.println(B[i]);
			}
		}

	}

}
