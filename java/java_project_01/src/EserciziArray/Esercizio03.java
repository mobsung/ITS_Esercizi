package EserciziArray;

public class Esercizio03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Esercizio n. 3 - copia metà array Creare un array A di n numeri interi,
		 * popolarlo dinamicamente SOLO per metà e stamparlo. Popolare poi la seconda
		 * metà con gli stessi valori della prima e stampare nuovamente. NB: per
		 * semplicità assumiamo che la dimensione dell’array sia un numero pari. Es.
		 * creo un array da 10 elementi e lo popolo con questi 5 valori (3, 5, 8, 2, 4).
		 * Alla fine l'array deve diventare (3, 5, 8, 2, 4, 3, 5, 8, 2, 4).
		 */
		
		int[] an = {
				11, 22, 33, 44, 55
		};
		
		int[] copy = new int [an.length * 2];
		
		for(int i = 0; i < copy.length; i++) {
			copy[i] = an[i % an.length];
		}
		
		for (int i = 0; i < copy.length; i++) {
			System.out.println(copy[i]);
		}
	}

}
