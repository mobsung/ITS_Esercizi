package traghetto;

public class TestTraghetto {
	public static void main(String[] args) {
		
		
		Biglietteria b = new Biglietteria();
		
		Persona p1 = new Persona("Marcel", "Movileanu", "MVC");
		Persona p2 = new Persona("Lorenzo", "Anzivino", "LZA");
		Persona p3 = new Persona("Stefano", "Reali", "SFR");
		Persona p4 = new Persona("Cristiano", "Coccia", "CR7");
		Persona p5 = new Persona("Nicol", "Shein", "NCS");
		Persona p6 = new Persona("Dario", "Montuoro", "DMT");
		traghetto.Persona p7 = new Persona("Daniele", "Gallo", "DNG");
		Persona p8 = new Persona("Matteo", "Fabbri", "MTF");
		
		Auto a1 = new Auto(Auto.TipoAuto.STANDARD, p1, "Targa1", 5);
		Moto m1 = new Moto(p2, "Targa2", 2);
		Tir t1 = new Tir(p3, "Targa3", 10, 3);
		try{
			a1.aggiungiPersona(p4);
			a1.aggiungiPersona(p5);
			t1.aggiungiPersona(p6);
		} catch (Exception e){
			System.out.println(e.getMessage());
		}

		b.aggiungiInCoda(a1);
		b.aggiungiInCoda(m1);
		b.aggiungiInCoda(t1);
		b.aggiungiInCoda(p7);
		b.aggiungiInCoda(p8);

		try{
			System.out.println(b.riceviPagamento());
			System.out.println(b.riceviPagamento());
			System.out.println(b.riceviPagamento());
			System.out.println(b.riceviPagamento());

		} catch (Exception e){
			System.out.println(e.getMessage());
		}

		System.out.println(b.getCassa());
		
	}
}
