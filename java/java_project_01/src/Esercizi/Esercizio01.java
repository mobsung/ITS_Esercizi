package Esercizi;

import java.util.Scanner;

public class Esercizio01 {
    public static void main(String[] args) {

        // Esercizio n. 1
        // Letti dalla tastiera due interi n > 0 e k > 0, stampare il valore di n^k.

        Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci due numeri interi:");

        int n = sc.nextInt();
        int k = sc.nextInt();

        int pow = 1;

        for (int i = 0; i < k; i++) {
            pow *= n;
        }

        System.out.println(n + " elevato a " + k + " equivale a " + pow);
        
        sc.close();
    }
}