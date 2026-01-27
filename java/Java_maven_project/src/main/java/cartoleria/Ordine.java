package cartoleria;

import java.util.ArrayList;
import java.util.Date;

public class Ordine {
	
	private Date data;
	private int numero;
	private Cliente cliente;
	private boolean pagato = false;
	private ArrayList<Articolo> merci = new ArrayList<>();
	
	public double calcolaTotale() {
		double totale = 0;
		
		for (Articolo a : merci) {
			totale += a.getPrezzoVendita();
		}
		return totale;
	}

	public void aggiungiArticolo(Articolo a){
		merci.add(a);
	}

	public void chiudiConto() {
		if (!pagato) {
			double totale = this.calcolaTotale();
			cliente.paga(totale);
			pagato = true;
		}
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

	public boolean isPagato(){
		return pagato;
	}
}
