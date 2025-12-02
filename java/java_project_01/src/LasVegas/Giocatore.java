package LasVegas;

public class Giocatore {


		private String nome;
		private double budget;
		private int puntata;
		private int numeroGiocato;
		
		
		public Giocatore(String nome, double budget) {
			this.nome = nome;
			this.budget = budget;
		}


		public String getNome() {
			return nome;
		}


		public void setNome(String nome) {
			this.nome = nome;
		}


		public double getBudget() {
			return budget;
		}


		public void setBudget(double budget) {
			this.budget = budget;
		}


		public int getPuntata() {
			return puntata;
		}


		public int getNumeroGiocato() {
			return numeroGiocato;
		}
		
		@Override
		public String toString() {
			return "Giocatore: nome= " + nome + ", budget= " + budget;
		}
		
		public void punta(int puntata, int numero) {
			if (budget - puntata >= 0) {
				this.puntata = puntata;
				this.numeroGiocato = numero;
				this.budget -= puntata;	
			}
		}
		
		public void incassa() {
			budget += (Dado.getRICARICO() * numeroGiocato);
		}
		
		public void reset() {
			puntata = 0;
			numeroGiocato = 0;
		}
		
		public void ricaricaBudget(int importo) {
			if (importo <= 0) {
				System.out.println("Non puoi ricaricare una quantita negativa");
			} else {
				budget += importo;
			}
		}
		
		public void recuperaPuntata() {
			budget += puntata;
			puntata = 0;
		}
}
