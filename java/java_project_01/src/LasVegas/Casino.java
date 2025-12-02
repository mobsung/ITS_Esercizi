package LasVegas;

public class Casino {
	/*
	 * Un casino’ ha un nome e un capitale iniziale
	 * 
	 * Il costruttore di Casino consente di personalizzare nome capitale iniziale
	 * 
	 * I principali metodi del casino’ sono valutaPuntate(int[] puntate) : boolean
	 * Riceve un array con tutte le puntate effettuate Ritorna la disponibilità di
	 * pagare true/false In caso true, incassa le puntate dei giocatori incassa
	 * (int importo) : void Incrementa il capitale della cifra indicata paga (int
	 * importo) : void decrementa il capitale di una cifra pari al prodotto del
	 * RICARICO per l’importo indicato
	 */
	
	private String nome;
	private int capitale;
	
	public Casino(String nome, int capitale) {
		this.nome = nome;
		this.capitale = capitale;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getCapitale() {
		return capitale;
	}

	public void setCapitale(int capitale) {
		this.capitale = capitale;
	}
	
	public boolean valutaPuntate(int[] puntate) {
		int sommaPuntate = 0;
		for (int puntata: puntate) {
			sommaPuntate += puntata;
		}
		if (sommaPuntate <= capitale) {
			return true;
		}
		return false;
	}
	
	public void incasso(int importo) {
		capitale += importo;
	}
	
	public void paga(int importo) {
		capitale -= (importo * Dado.getRICARICO());
	}

	@Override
	public String toString() {
		return "Casino: nome=" + nome + ", capitale=" + capitale;
	}
	
	
}
