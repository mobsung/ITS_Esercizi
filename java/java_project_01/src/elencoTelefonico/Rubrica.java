package elencoTelefonico;

import java.util.ArrayList;

public class Rubrica {
	private ArrayList <Contatto> contatti = new ArrayList<>();
	private int dimensione;
	
	
	public Rubrica(int dimensione) {
		super();
		this.dimensione = dimensione;
	}


	public int getDimensione() {
		return dimensione;
	}


	public void setDimensione(int dimensione) {
		this.dimensione = dimensione;
	}


	public ArrayList<Contatto> getContatti() {
		return contatti;
	}
	
	public void inserisciContatto(Contatto contatto) {
		if (contatti.size() < dimensione) {
			contatti.add(contatto);
		} else {
			System.out.println("Spazio superato");
		}
	}
	
	public void mostraPosizione(int posizione) {
		contatti.get(posizione);
	}

	public String elencoContatti() {
		String s = "Elenco contatti\n";
		
		for (Contatto c : contatti) {
			s += c.toString() + "\n";
		}
		
		return s;
	}
	
	public int mostraNumeroContatti() {
		return contatti.size();
	}
	
	public int mostraNumeroPostiLiberi() {
		return dimensione - contatti.size();
	}
	
	public Contatto cercaContattoPerNome(String nome) throws Exception {
		for (Contatto c : contatti) {
			if (c.getNome().equals(nome)) {
				return c;
			}
		}
		throw new Exception();
	}
	
	public Contatto cercaContattoPerNumero(String numero) throws Exception {
		for (Contatto c : contatti) {
			if (c.getNumero().equals(numero)) {
				return c;
			}
		}
		throw new Exception();
	}
}
