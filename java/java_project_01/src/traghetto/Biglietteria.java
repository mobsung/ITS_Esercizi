package traghetto;

import java.util.ArrayList;

public class Biglietteria {
	
	private ArrayList<Tariffabile> coda = new ArrayList<>();
	private double cassa = 0;
	
	public void aggiungiInCoda(Tariffabile t) {
		coda.add(t);
	}
	
	public Tariffabile riceviPagamento() throws Exception{
		
		if (coda.size() == 0) {
			throw new Exception("La coda è vuota");
		} else {
			cassa += coda.get(0).calcolaTariffa();
			return coda.remove(0);
		}
		
	}

	public double getCassa() {
		return cassa;
	}
	
	
}
