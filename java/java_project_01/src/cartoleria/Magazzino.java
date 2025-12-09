package cartoleria;

import java.util.ArrayList;

public class Magazzino {
	
	private ArrayList <Articolo> articoli = new ArrayList<>();
	
	public void aggiungiArticolo(Articolo articolo) {
		articoli.add(articolo);
	}
	
	
	public void rimuoviElemento(Articolo articolo) {
		articoli.remove(articolo);
	}
	
	public void mostraArticoli() {
		String s = "";
		
		for(Articolo a : articoli) {
			s += a.toString();
			}
		System.out.println(s);
	}
	
	public void mostraCostiTotali() {
		int s = 0;
		for (Articolo a : articoli) {
			s += a.getCosto();
		}
		System.out.println("Costo totale articoli: " + s + " $");
	}
	
	public void mostraRicaviTotali() {
		int s = 0;
		for (Articolo a : articoli) {
			s += a.getPrezzoVendita();
		}
		System.out.println("Ricavi totali: " + s + " $");
	}
	
	public void ricercaPerMarca(String marca) {
		String s = "Articoli appartenenti che hanno la marca: " + marca + "\n";
		
		for (Articolo a : articoli) {
			if (a.getMarca() == marca) {		
				s += "- " + a.toString() + "\n";
			}
		}
		System.out.println(s);
	}
	
	public void ricercaPerModello(String modello) {
		String s = "Articoli appartenenti che hanno il modello: " + modello + "\n";
		
		for (Articolo a : articoli) {
			if (a.getModello() == modello) {	
				s += "- " + a.toString() + "\n";
			}
		}
		System.out.println(s);
	}
	
	
	public void ordinaArticoliPerCosto() {
		int iterations = articoli.size() - 1;
		while (iterations > 0) {
			for (int i = 0; i < iterations; i++) {
				if (articoli.get(i).getCosto() > articoli.get(i + 1).getCosto()) {
					Articolo temp = articoli.get(i + 1);
					articoli.set(i + 1, articoli.get(i));
					articoli.set(i,  temp);
				}
			}
			iterations -= 1;
		}
	}
	
	public void ordinaArticoliPerPrezzo() {
		int iterations = articoli.size() - 1;
		while (iterations > 0) {
			for (int i = 0; i < iterations; i++) {
				if (articoli.get(i).getPrezzoVendita() > articoli.get(i + 1).getPrezzoVendita()) {
					Articolo temp = articoli.get(i + 1);
					articoli.set(i + 1, articoli.get(i));
					articoli.set(i,  temp);
				}
			}
			iterations -= 1;
		}
	}
}
