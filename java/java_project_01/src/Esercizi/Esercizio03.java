package Esercizi;

import java.util.Scanner;

public class Esercizio03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Esercizio n. 3
		// Letto dalla tastiera un numero intero n > 0, stampare il fattoriale di n.
		// Definizione di fattoriale: per n>1
		// n! = n * ( n -1 ) * ( n -2 )... * 1.
		// Per n= 1, n! = 1

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int fattoriale = 1;

		for (int i = 0; i < n; i++) {
			fattoriale *= n - i;
		}
		System.out.println(fattoriale);
		sc.close();
	}

}
