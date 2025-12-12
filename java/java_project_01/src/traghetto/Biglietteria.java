package traghetto;

import java.util.ArrayList;

public class Biglietteria {
	
	private ArrayList<Tariffabile> coda = new ArrayList<>();
	private double cassa = 0;
	
	public void aggiungiInCoda(Tariffabile t) {
		coda.add(t);
	}
	
	public Tariffabile riceviPagamento() throws ArithmeticException{
		
		if (coda.size() == 0) {
			throw new ArithmeticException("La coda è vuota");
		} else {
			cassa += coda.get(0).calcolaTariffa();
			Tariffabile entità =  coda.remove(0);
			return entità;
		}
		
	}

	public double getCassa() {
		return cassa;
	}
	
	
}
