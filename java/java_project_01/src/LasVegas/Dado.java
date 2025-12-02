package LasVegas;

import java.util.Random;

public class Dado {
	/*
	 * Un dado ha 6 facce
	 * 
	 * Il costruttore del Dado crea un dado
	 * 
	 * Il dado dispone di una costante RICARICO che indica il ricarico sulla
	 * puntata. E’ impostata a 5.
	 * 
	 * Il metodo per lanciare il dado è estrai() : int Genera un numero intero
	 * casuale compreso tra 1 e 6 Ritorna il numero estratto
	 */
	
	private int facce = 6;
	private static final int RICARICO = 5;
	
	
	public int getFacce() {
		return facce;
	}
	
	public static int getRICARICO() {
		return RICARICO;
	}
	
	public int estrai() {
		Random r = new Random();
		
		return r.nextInt(1, facce + 1);
	}
	
	
}
