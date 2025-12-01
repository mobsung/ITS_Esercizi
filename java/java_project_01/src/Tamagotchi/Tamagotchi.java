package Tamagotchi;

public class Tamagotchi {
	
	enum Specie {
		CANE,
		GATTO,
		CANARINO,
		CONIGLIO;
	}
	
	private final String nome;
	private final Specie specie;
	private double peso;
	private int altezza;
	private int energia;
	
	
	public Tamagotchi(String nome, Specie specie) {
		this.nome = nome;
		this.specie = specie;
		this.setPesoAltezzaEnergia();
	}


	public Tamagotchi(String nome) {
		this.nome = nome;
		this.specie = Specie.CANE;
		this.setPesoAltezzaEnergia();
	}
	
	public String getNome() {
		return nome;
	}


	public Specie getSpecie() {
		return specie;
	}


	public double getPeso() {
		return peso;
	}


	public int getAltezza() {
		return altezza;
	}


	public int getEnergia() {
		return energia;
	}

	@Override
	public String toString() {
		return "Tamagotchi: nome=" + nome + ", specie=" + specie + ", peso=" + peso + ", altezza=" + altezza
				+ ", energia=" + energia;
	}


	private void setPesoAltezzaEnergia() {
		switch(this.specie) {
		case Specie.CANE:
			this.altezza = 20;
			this.peso = 300;
			break;
		case Specie.GATTO:
			this.altezza = 10;
			this.peso = 100;
			break;
		case Specie.CANARINO:
			this.altezza = 3;
			this.peso = 10;
			break;
		case Specie.CONIGLIO:
			this.altezza = 10;
			this.peso = 100;
			break;
		}
		this.energia = 3;
	}
	
	
	private boolean hasEnergia() {
		if (this.energia > 1 && this.energia < 10) {
			return true;
		}
		return false;
	}
	
	public boolean mangia() {
		if (this.hasEnergia()) {
			this.altezza ++;
			this.peso *= 1.15;
			this.energia ++;
			return true;
		} 
		return false;
	}
	
	public boolean dorme() {
		if (this.hasEnergia()) {
			this.energia ++;
			return true;
		}
		return false;
	}
	
	public boolean gioca() {
		if (this.hasEnergia()) {
			this.peso *= 0.9;
			this.energia --;
			return true;
		}
		return false;
	}
	
}
