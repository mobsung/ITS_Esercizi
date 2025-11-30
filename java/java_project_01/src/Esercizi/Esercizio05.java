package Esercizi;

import java.util.Scanner;

public class Esercizio05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Esercizio n. 5 (Perimetro del triangolo)
//		Siano dati 2 punti nel piano cartesiano A (x1, y1) e B (x1, y2).
//		Considerare il triangolo rettangolo che si ottiene aggiungendo il punto C(x2,y1).
//		Scrivere un programma che legge in ingresso i valori x1, y1 e x2, y2, calcola e stampa il perimetro del triangolo ottenuto secondo le regole suddette.
//		Esempio: se x1 = 1, y1 = 1 e x2 = 2, y2= 2 allora il perimetro sarà 3.414213562373095
//		Nota: utilizzare le funzioni della libreria matematica Math per calcolare potenze, radici quadrate, ecc
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Inserisci 4 punti: x1, y1 e x2, y2");
		int x1 = sc.nextInt();
        int y1 = sc.nextInt();
		int x2 = sc.nextInt();
        int y2 = sc.nextInt();
        
        int b = Math.abs(x1 - x2);
        int h = Math.abs(y1 - y2);
		double i = Math.sqrt(Math.pow(b, 2) + Math.pow(h, 2));
		
		double perimetro = b + h + i;
		System.out.println("Perimetro = "+perimetro);
        
		sc.close();
	}

}
