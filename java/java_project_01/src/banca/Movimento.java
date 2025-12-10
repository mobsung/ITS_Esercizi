package banca;

import java.util.Date;

public class Movimento {
	
	public enum TipoMovimento {
		PRELIEVO,
		VERSAMENTO
	}
	
	private TipoMovimento tipoMovimento;
	private Date data;
	private double ammontare;
	
	
	public Movimento(String tipoMovimento, Date data, double ammontare) {
		super();
		setTipoMovimento(tipoMovimento);
		this.data = data;
		setAmmontare(ammontare);
	}


	@Override
	public String toString() {
		return "tipoMovimento=" + tipoMovimento + ", data=" + data + ", ammontare=" + ammontare;
	}


	public double getAmmontare() {
		return ammontare;
	}


	private void setAmmontare(double ammontare) {
		if (ammontare > 0) {	
			this.ammontare = ammontare;
		} else {
			System.out.println("Devi inserire un importo Positivo");
		}
	}
	
	private void setTipoMovimento(String tipoMovimento) {
		try {
		    TipoMovimento movimento = TipoMovimento.valueOf(tipoMovimento.toUpperCase());
		    this.tipoMovimento = movimento;
		} catch (IllegalArgumentException e) {
		    System.out.println("Tipo di movimento non valido: " + tipoMovimento);
		}

	}

	public TipoMovimento getTipoMovimento() {
		return tipoMovimento;
	}


	public Date getData() {
		return data;
	}
	
	
	
	
	
}
