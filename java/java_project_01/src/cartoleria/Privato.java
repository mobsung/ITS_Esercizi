package cartoleria;

public class Privato extends Cliente {
	
	private double denaro;

	public Privato(String nome, double denaro) {
		super(nome);
		this.denaro = denaro;
	}
	
	@Override
	public void paga(double ammontare) {
		denaro -= ammontare;
	}
}
