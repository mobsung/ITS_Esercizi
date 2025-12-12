package traghetto;

import java.util.Objects;

public class Persona implements Tariffabile{
	
	private String nome;
	private String cognome;
	private String CF;
	
	public Persona(String nome, String cognome, String CF) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.CF = CF;
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(CF);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Persona other = (Persona) obj;
		return Objects.equals(CF, other.CF);
	}

	public String getNome() {
		return nome;
	}

	public String getCognome() {
		return cognome;
	}

	public String getCF() {
		return CF;
	}


	@Override
	public double calcolaTariffa() {
		return 2.5;
	}

	@Override
	public String toString() {
		return "| nome=" + nome + ", cognome=" + cognome + ", CF=" + CF;
	}
	
}
