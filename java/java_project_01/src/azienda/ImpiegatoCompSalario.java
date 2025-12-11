package azienda;

import java.util.Comparator;

public class ImpiegatoCompSalario implements Comparator<Impiegato> {

	@Override
	public int compare(Impiegato o1, Impiegato o2) {
		// criterio che induce l'ordinamento per salario
		if(o1.getSalario() > o2.getSalario()) {
			return 1;
		}
		else if (o2.getSalario() > o1.getSalario()) {
			return -1;
		}
		else
			return 0;
	}

}