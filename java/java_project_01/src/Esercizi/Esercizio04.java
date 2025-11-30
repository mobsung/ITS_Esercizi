package Esercizi;

import java.util.Scanner;

public class Esercizio04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Esercizio n. 4 (Quadrato o rettangolo?)
		//Siano dati 2 punti nel piano cartesiano A (x1, y1) e B (x2, y2).
		//Considerare il parallelogramma che si ottiene aggiungendo il punto C(x1, y2) e il punto D (x2, y1) e congiungendo i 4 punti nell’ordine A,C,B,D
		//Scrivere un programma che legge in ingresso i valori x1, y1 e x2, y2, verifica se si può ottenere un quadrato oppure se si tratta di un generico rettangolo. 
		//Stampa questo risultato e in base alla figura rilevata, calcola e stampa il perimetro e l’area della figura.
		//Nota: utilizzare le funzioni della libreria matematica Math per calcolare potenze, radici quadrate, ecc
		
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Inserisci 4 punti: x1, y1 e x2, y2");
		int x1 = sc.nextInt();
        int y1 = sc.nextInt();
		int x2 = sc.nextInt();
        int y2 = sc.nextInt();

        int b = Math.abs(x1 - x2);
        int h = Math.abs(y1 - y2);
        
        int perimetro = b * 2 + h * 2;
        int area = (b * h) / 2; 
        
        if(b == h) {
        	System.out.println("Hai ottenuto un quadrato");
        }else {
        	System.out.println("Hai ottenuto un rettangolo");
        }
        System.out.println("Con perimetro = "+ perimetro);
    	System.out.println("Con area = "+ area);
        
        
    	sc.close();
		
	}

}
