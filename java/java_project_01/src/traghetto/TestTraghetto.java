package traghetto;

import traghetto.Auto.TipoAuto;

public class TestTraghetto {
	public static void main(String[] args) {
		
		
		Biglietteria b = new Biglietteria();
		
		Persona p1 = new Persona("Marcel", "Movileanu", "MVC");
		Persona p2 = new Persona("Lorenzo", "Anzivino", "LZA");
		Persona p3 = new Persona("Stefano", "Reali", "SFR");
		Persona p4 = new Persona("Cristiano", "Coccia", "CR7");
		Persona p5 = new Persona("Nicol", "Shein", "NCS");
		Persona p6 = new Persona("Dario", "Montuoro", "DMT");
		Persona p7 = new Persona("Daniele", "Gallo", "DNG");
		Persona p8 = new Persona("Matteo", "Fabbri", "MTF");
		
		Auto a1 = new Auto(TipoAuto.STANDARD, p1, "Targa1", 5);
		Moto m1 = new Moto(p2, "Targa2", 2);
		Tir t1 = new Tir(p3, "Targa3", 10, 3);
		
		a1.aggiungiPersona(p4);
		a1.aggiungiPersona(p5);
		t1.aggiungiPersona(p6);
		
		b.aggiungiInCoda(a1);
		b.aggiungiInCoda(m1);
		b.aggiungiInCoda(t1);
		b.aggiungiInCoda(p7);
		b.aggiungiInCoda(p8);
		
		System.out.println(b.riceviPagamento());
		System.out.println(b.riceviPagamento());
		System.out.println(b.riceviPagamento());
		System.out.println(b.riceviPagamento());
		
		System.out.println(b.getCassa());
		
	}
}
