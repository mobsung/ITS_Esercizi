package banca;

import java.util.ArrayList;
import java.util.Date;
import java.util.Objects;

public class Standard {
	
	private String intestatario;
	private int numero;
	private double saldo;
	private ArrayList<Movimento> movimenti = new ArrayList<>();
	
	
	
	public ArrayList<Movimento> getMovimenti() {
		return movimenti;
	}

	public Standard(String intestatario, int numero) {
		super();
		this.intestatario = intestatario;
		this.numero = numero;
	}
	
	public Standard(String intestatario, int numero, double saldo) {
		this(intestatario, numero);
		this.saldo = saldo;
	}
	
	public void setSaldo(double ammontare) {
		saldo = ammontare;
	}
	
	public String getIntestatario() {
		return intestatario;
	}

	public int getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}

	public boolean checkBalance(double ammontare) {
		if (saldo - ammontare < saldo) {
			return false;
		}
		return true;
	}
	
	public void movimento(String tipoMovimento, double ammontare, Date data) {
		
		if (!(tipoMovimento.equalsIgnoreCase("prelievo") && checkBalance(ammontare))) {
			System.out.println("Non hai sufficiente saldo per prelevare");
		} else {
			Movimento movimento = new Movimento(tipoMovimento, data, ammontare);
			movimenti.add(movimento);
		}
	}
	
	public void datiConto() {
		System.out.println("Dati conto\n"+"Intestatario: " + intestatario + "\nNumero conto: " + numero + "\nSaldo: "  + saldo);
	}
	
	public void listaMovimenti() {
		String s = "Lista movimenti\n";
		
		for (Movimento m : movimenti) {
			s += m.toString() + "\n";
		}
		
		System.out.println(s);
	}

	@Override
	public int hashCode() {
		return Objects.hash(numero);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Standard other = (Standard) obj;
		return numero == other.numero;
	}
	
	
}
