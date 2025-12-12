package traghetto;

public class Moto extends Veicolo {


	public Moto(Persona p, String targa, int posti) {
		super(p, targa, posti);
	}

	@Override
	public double calcolaTariffa() {
		return 3.5 + (getPersone().get(0).calcolaTariffa() * postiOccupati());
	}
}