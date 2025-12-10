package banca;

import java.util.ArrayList;
import java.util.Date;

public class Bank {
	
	private double capitale;
	private String nome;
	private ArrayList<Standard> conti = new ArrayList<>();
	
	
	public Bank(double capitale, String nome) {
		super();
		this.capitale = capitale;
		this.nome = nome;
	}
	
	public void open(Standard conto) {
		conti.add(conto);
	}
	
	public void close(Standard conto) {
		conti.remove(conto);
	}
	
	public void trasferisci(Standard ordinante, Standard beneficiario, double ammontare, Date data) {
		if (conti.contains(ordinante) && conti.contains(beneficiario)) {
			ordinante.movimento("versamento", ammontare, data);
			beneficiario.movimento("prelievo", ammontare,  data);
		}
	}
}
