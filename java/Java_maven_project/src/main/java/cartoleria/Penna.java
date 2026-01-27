package cartoleria;

public class Penna extends Articolo{

	private String colore;
	
	public Penna(String id, String marca, String modello, int costo, String colore) {
		super(id, marca, costo, modello);
		this.colore = colore;
	}

	public String getColore() {
		return colore;
	}

	public void setColore(String colore) {
		this.colore = colore;
	}

	@Override
	public String toString() {
		return super.toString() + "colore=" + colore;
	}
	
}
