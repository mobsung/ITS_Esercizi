package Esercizi;

import java.util.Scanner;

public class Esercizio02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Esercizio n. 2 (Sommatoria)
		//Scrivere un programma che legge dalla tastiera due interi n >0 e k >0 e stampa il risultato della sommatoria 
		//k + k2+ k3+...+ kn.
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Inserisci due numeri interi:");

        int n = sc.nextInt();
        int k = sc.nextInt();
        
        int sommatoria = 0;
        
        for (int i = 0; i < k; i++) {
        	
        	int pow = 1;
        	
        	for (int j = 0; j <= i; j++) {
        		pow *= n;
        	}
        		
        	sommatoria += pow;
        }
        
        System.out.println("sommatoria = "+sommatoria);
        
        sc.close();
		
	}

}
