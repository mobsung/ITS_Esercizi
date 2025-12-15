package traghetto;

public class Auto extends Veicolo{
	
	
	public enum TipoAuto{
		MINI(4),
		STANDARD(5),
		SUV(8.5);
		
		private final double tariffa;
		
		private TipoAuto(double tariffa) {
			this.tariffa = tariffa;	
		}
		
		public double getTariffa() {
			return tariffa;
		}
	}
	
	
	private TipoAuto tipoAuto;
	

	public Auto(TipoAuto tipoAuto, Persona p, String targa, int posti) {
		super(p, targa, posti);
		this.tipoAuto = tipoAuto;
	}

	@Override
	public String toString() {
		return "tipoAuto=" + tipoAuto + " " + super.toString();
	}
	
	@Override
	public double calcolaTariffa() {
		return tipoAuto.getTariffa() + (getPersone().get(0).calcolaTariffa() * postiOccupati());
	}


}
