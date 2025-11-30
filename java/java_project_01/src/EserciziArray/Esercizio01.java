package EserciziArray;


public class Esercizio01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Esercizio n. 1 – copia array Letto in input un array A di n numeri interi,
		 * creare un secondo array della stessa dimensione e popolarlo copiando tutti
		 * gli elementi del primo
		 */
		
		int[] anonimous = {
				1, 2, 3, 4, 5
		};
		
		int[] copy = new int[anonimous.length];
		
		for(int i = 0; i < anonimous.length; i++) {
			copy[i] = anonimous[i];
		}
		
		for (int i = 0; i < copy.length; i++) {
			System.out.println(copy[i]);
		}
	}

}
