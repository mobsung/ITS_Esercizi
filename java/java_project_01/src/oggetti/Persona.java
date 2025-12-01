package oggetti;

public class Persona {
	
	// dichiarazione attributi	
	private String nome;
	private int eta;
	private double peso;
	
	// costruttori
	public Persona(String nome, int eta, double peso) {
		this.nome = nome;
		this.eta = eta;
		this.peso = peso;
	}
	
	// bambini appena nati con parametro eta a 0 in questo caso default
	public Persona(String nome, double peso) {
		this.nome = nome;
		this.peso = peso;
	}

	// metodi getter e setter
	public String getNome() {
		return nome;
	}

	public int getEta() {
		return eta;
	}

	public void setEta(int eta) {
		this.eta = eta;
	}

	public double getPeso() {
		return peso;
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	@Override
	public String toString() {
		return "Persona [nome=" + nome + ", eta=" + eta + ", peso=" + peso + "]";
	}
	
	
}
