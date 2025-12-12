package traghetto;

public class Tir extends Veicolo{

	private double merce;
	
	public Tir(Persona p, String targa, double merce, int posti) {
		super(p, targa, posti);
		this.merce = merce;

	}

	@Override
	public String toString() {
		return super.toString() + " merce=" + merce;
	}

	@Override
	public double calcolaTariffa() {
		return 12.5 + (getPersone().get(0).calcolaTariffa() * postiOccupati()) + (merce * 0.5);
	}
}
