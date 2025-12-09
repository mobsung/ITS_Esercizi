package azienda;

import java.util.Date;

public class Manager extends Impiegato {

	private String segretaria;

	public Manager(String nome, double salario, Date dataAssunzione, String segretaria) {
		super(nome, salario, dataAssunzione);
		this.setSegretaria(segretaria);
	}

	public String getSegretaria() {
		return segretaria;
	}

	public void setSegretaria(String segretaria) {
		this.segretaria = segretaria;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + ", segretaria = " + segretaria;
	}

	@Override
	public void incrSalario(double aumento) {
		// calcolo del bonus
		Date oggi = new Date();
		double bonus = 0.5*(oggi.getYear() +1900 - this.getAnnoAssunzione());
		
		super.incrSalario(aumento + bonus);
	}
	
	
	
}