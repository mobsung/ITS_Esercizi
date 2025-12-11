package prenotazioniCamere;


public class Reservation implements Comparable<Reservation>{
	
	private String nome;
	private int dataInizio;
	private int dataFine;
	
	
	public Reservation(String nome, int dataInizio, int dataFine) {
		super();
		this.nome = nome;
		this.dataInizio = dataInizio % 365;
		this.dataFine = dataFine & 365;
	}


	public String getName() {
		return nome;
	}


	public int getDataInizio() {
		return dataInizio;
	}


	public int getDataFine() {
		return dataFine;
	}


	@Override
	public String toString() {
		return "nome=" + nome + ", dataInizio=" + dataInizio + ", dataFine=" + dataFine;
	}


	public boolean compreso(Reservation o) {
		if (o.dataInizio <= this.dataFine && o.dataFine >= this.dataInizio) {
			return true;
		}
		return false;
	}

	@Override
	public int compareTo(Reservation o) {
		if (this.dataInizio < o.dataInizio) {
			return -1;
		} else if (this.dataInizio == o.dataInizio) {
			return 0;
		}
		return 1;
	}
	
}
