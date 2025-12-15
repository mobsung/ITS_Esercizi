package traghetto;

import java.util.ArrayList;

public abstract class Veicolo implements Tariffabile{
	

	private ArrayList<Persona> persone = new ArrayList<>();
	private String targa;
	private int posti;
	
	
	
	public Veicolo(Persona p, String targa, int posti) {
		super();
		persone.add(p);
		this.targa = targa;
		this.posti = posti;
	}
	
	@Override
	public String toString() {
		return "persone=" + persone + ", targa=" + targa + ", posti=" + posti;
	}

	public ArrayList<Persona> getPersone() {
		return persone;
	}
	
	public int postiOccupati() {
		return persone.size();
	}
	
	public void aggiungiPersona(Persona p) throws Exception{
		if (postiOccupati() < posti) {
			persone.add(p);
		} else {

			throw new Exception("Raggiunto il limite di posti occupati");
		}
		
	}

	public void rimuoviPersona(Persona p) throws Exception{
		if (postiOccupati() > 1) {
			persone.remove(p);
		} else {
			throw new Exception("Il veicolo deve contenere almento una persona");
		}
		
	}
}
