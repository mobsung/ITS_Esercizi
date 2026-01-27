package cartoleria;

public abstract class Cliente {
	
	private String nome;

	public Cliente(String nome) {
		super();
		this.nome = nome;
	}
	
	public abstract void paga(double ammontare);
	
}
