package EserciziArray;

public class Esercizio02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Esercizio n. 2 - inversione array Letto in input un array A di n numeri
		 * interi, creare un secondo array B della stessa dimensione e popolarlo
		 * invertendo l’ordine degli elementi del primo. Esempio: se A è (10,27,13, 4),
		 * allora devo ottenere B (4,13,27,10) Al termine dell’elaborazione stampare gli
		 * array A e B.
		 */
		
		int[] anonimous = {
				1, 2, 3, 4, 5
		};
		
		int[] copy = new int[anonimous.length];
		
		
		for(int i = anonimous.length - 1; i >= 0; i--) {
			
			copy[anonimous.length - 1 - i] = anonimous[i];
		}
		
		for (int i = 0; i < copy.length; i++) {
			System.out.println(copy[i]);
		}
	}

}
