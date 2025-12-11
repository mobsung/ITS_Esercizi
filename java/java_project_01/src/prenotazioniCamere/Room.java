package prenotazioniCamere;

import java.util.ArrayList;
import java.util.Collections;

public class Room {
	
	private int numero;
	private ArrayList<Reservation> reservations = new ArrayList<>();
	
	public int getNumero() {
		return numero;
	}

	public Room(int numero) {
		super();
		this.numero = numero;
	}

	@Override
	public String toString() {
		return "numero=" + numero;
	}

	public Reservation reserve(String nome, int dataInizio, int dataFine) throws ArithmeticException{
		Reservation res = new Reservation(nome, dataInizio, dataFine);
		
		reservations.forEach((r) -> {
			if (r.compreso(res)) {
				throw new ArithmeticException("I giorni richiesti sono già occupati");
			}
		});
		
		reservations.add(res);
		return res;
		
	}
	
	public ArrayList<Reservation> reservations() {
		
		Collections.sort(reservations);
		return reservations;
	}
	
}
