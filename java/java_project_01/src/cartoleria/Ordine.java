package cartoleria;

import java.util.ArrayList;
import java.util.Date;

public class Ordine {
	
	private Date data;
	private int numero;
	private Cliente cliente;
	private ArrayList<Articolo> merci = new ArrayList<>();
	
	public double calcolaTotale() {
		double totale = 0;
		
		for (Articolo a : merci) {
			totale += a.getPrezzoVendita();
		}
		return totale;
	}
	
	public void chiudiConto() {
		double totale = this.calcolaTotale();
		
		cliente.paga(totale);
	}

	public Date getData() {
		return data;
	}

	public int getNumero() {
		return numero;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public ArrayList<Articolo> getMerci() {
		return merci;
	}
}
