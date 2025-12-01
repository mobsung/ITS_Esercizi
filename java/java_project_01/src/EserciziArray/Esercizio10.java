package EserciziArray;

public class Esercizio10 {
	
	
	public static void sortB(int[] array){
		int iterations = array.length - 1;
		
		while (iterations > 0) {
			for (int i = 0; i < iterations; i++) {
				if (array[i] > array[i + 1]) {
					int temp = array[i + 1];
					array[i + 1] = array[i];
					array[i] = temp;
				}

			}
			
			iterations -= 1;
			
		}
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
		 * Esercizio n. 10 – ordinamento Dato in input un array di numeri interi,
		 * implementare l’algoritmo del Bubblesort per ordinarlo. Alla fine stampare
		 * l’array ordinato.
		 * 
		 * Il Bubblesort è un famoso algoritmo di ordinamento. Lo scopo è l’ordine
		 * crescente. L'insieme di dati viene scansionato, ogni coppia di elementi
		 * adiacenti viene comparata ed i due elementi vengono invertiti di posizione se
		 * sono nell'ordine sbagliato. Eseguita la prima scansione l’elemento più GRANDE
		 * viene posizionato definitivamente alla fine dell’array. Quindi si procede con
		 * la scansione del sotto elenco ottenuto ignorando l’elemento già posizionato.
		 * Dopo aver eseguito un numero di scansioni pari alla (lunghezza – 1)
		 * dell’array, l’elenco è sicuramente ordinato.
		 */

		int[] mixed = { 7, 11, 1, 4, 20, 3, 5, 6, 13 };
		
		Esercizio10.sortB(mixed);
		
		for (int i = 0; i < mixed.length; i++) {
			System.out.print(mixed[i] + " ");
		}

	}

}
