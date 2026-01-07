package azienda;

import java.util.Comparator;

public class ImpiegatoCompSalario implements Comparator<Impiegato> {

	@Override
	public int compare(Impiegato o1, Impiegato o2) {
		// criterio che induce l'ordinamento per salario
        return Double.compare(o1.getSalario(), o2.getSalario());
	}

}