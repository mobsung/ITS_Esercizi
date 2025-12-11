package azienda;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;


public class EsempioOrdinamenti {

	public static void main(String[] args) {
		// ordino una lista di stringhe
		
		
		// ordino una lista di impiegati
		ArrayList<Impiegato> listaImp = new ArrayList<>();
		listaImp.add(new Impiegato("mario", 1500, new Date()));
		listaImp.add(new Impiegato("anna", 1500, new Date(120, 1, 1)));   // 2020
		listaImp.add(new Impiegato("giorgio", 2500, new Date(110, 1, 1)));  //2010
		listaImp.add(new Impiegato("manuel", 1200, new Date()));
		
		Collections.sort(listaImp);
		
		for (Impiegato impiegato : listaImp) {
			System.out.println(impiegato);
		}
		
		System.out.println("------------------------------------------------");
		
		Collections.sort(listaImp, new ImpiegatoCompSalario());
		for (Impiegato impiegato : listaImp) {
			System.out.println(impiegato);
		}
		
		System.out.println("------------------------------------------------");
		
		Collections.sort(listaImp, new ImpiegatoCompData());
		for (Impiegato impiegato : listaImp) {
			System.out.println(impiegato);
		}
		
	}

}