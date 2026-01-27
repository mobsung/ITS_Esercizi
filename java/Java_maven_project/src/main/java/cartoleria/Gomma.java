package cartoleria;

public class Gomma extends Articolo{
	
	private int dimensione;
	private String forma;

	public Gomma(String id, String marca, String modello, int costo, int dimensione, String forma) {
		super(id, marca, costo, modello);
		this.dimensione = dimensione;
		this.forma = forma;
	}

	public int getDimensione() {
		return dimensione;
	}

	public void setDimensione(int dimensione) {
		this.dimensione = dimensione;
	}

	public String getForma() {
		return forma;
	}

	public void setForma(String forma) {
		this.forma = forma;
	}

	@Override
	public String toString() {
		return super.toString() + "dimensione=" + dimensione + ", forma=" + forma;
	}
	
	
	
}
