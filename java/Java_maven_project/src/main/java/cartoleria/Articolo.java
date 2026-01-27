package cartoleria;

import java.util.Objects;

public class Articolo {
	
	private String marca;
	private String modello;
	private final String id;
	private int costo;
	private int prezzoVendita;
	
	
	public Articolo(String marca, String modello, int costo, String id) {
		super();
		this.id = id;
		this.marca = marca;
		this.modello = modello;
		this.costo = costo;
		this.setPrezzoVendita();
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Articolo other = (Articolo) obj;
		return Objects.equals(id, other.id);
	}

	public String getId() {
		return this.id;
	}
	
	public int getCosto() {
		return costo;
	}


	public void setCosto(int costo) {
		this.costo = costo;
	}


	public int getPrezzoVendita() {
		return prezzoVendita;
	}


	public void setPrezzoVendita() {
		this.prezzoVendita = costo * 2;
	}


	public String getMarca() {
		return marca;
	}


	public String getModello() {
		return modello;
	}


	@Override
	public String toString() {
		return "marca=" + marca + ", modello=" + modello + ", costo=" + costo + ", prezzoVendita=" + prezzoVendita;
	}
	
	
}
