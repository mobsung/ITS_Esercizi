package EserciziArray;

public class Esercizio11 {
	public static void main(String[] args) {
		/*
		 * Esercizio n. 11 (Fusione tra due array ordinati) Letti da tastiera 2 array di
		 * numeri interi, eseguire l’ordinamento col metodo precedente. Quindi creare un
		 * terzo array che abbia l’unione degli elementi e mantenga l'ordinamento. NB:
		 * se un elemento fosse presente in entrambi gli array, nel terzo array deve
		 * comparire una sola volta
		 */

		int[] a = { 7, 11, 1, 4, 20 };
		int[] b = { 1, 2, 3, 4, 5 };
		int[] c = new int[a.length + b.length];

		for (int i = 0; i < c.length; i++) {
			if (i < a.length) {
				c[i] = a[i];
			} else {
				boolean valido = true;
				for (int j = 0; j < a.length; j++) {
					if (b[i - a.length] == a[j]) {
						valido = false;
						break;
					}
				}
				if (valido) {
					c[i] = b[i - a.length];
				}
			}
		}

		Esercizio10.sortB(c);
		
		for (int i = 0; i < c.length; i++) {
			System.out.print(c[i] + " ");
		}
	
	}
}
