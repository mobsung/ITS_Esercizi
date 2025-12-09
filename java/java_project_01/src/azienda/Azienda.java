package azienda;

import java.util.ArrayList;

public class Azienda {

	private String nome;
	private ArrayList<Impiegato> elencoDipendenti;
	
	public Azienda(String nome) {
		super();
		this.nome = nome;
		this.elencoDipendenti = new ArrayList<>();
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public ArrayList<Impiegato> getElencoDipendenti() {
		return elencoDipendenti;
	}

	@Override
	public String toString() {
		//return "Azienda [nome=" + nome + ", elencoDipendenti=" + elencoDipendenti.toString() + "]";
		
		String s = "Nome azienda: " + nome + "\n";
		
		for (Impiegato impiegato : elencoDipendenti) {
			s += impiegato.toString() + "\n";
		}
		
		return s;
	}
	
	public void assume(Impiegato impiegato) {
		this.elencoDipendenti.add(impiegato);
		
	}
	
	public void incrSalarioPerTutti(double aumento) {
		for(int i= 0; i < elencoDipendenti.size(); i++) {
			elencoDipendenti.get(i).incrSalario(aumento);
		}
	}
	
	
}