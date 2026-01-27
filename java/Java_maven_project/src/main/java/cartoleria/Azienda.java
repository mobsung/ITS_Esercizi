package cartoleria;

public class Azienda extends Cliente {
	
	private double conto;
	
	public Azienda(String nome, double conto) {
		super(nome);
		this.conto = conto;
	}

	public double getConto() {
		return conto;
	}

	@Override
	public void paga(double ammontare) {
		conto -= ammontare;
	}
	
}
