package azienda;

import java.util.Comparator;

public class ImpiegatoCompData implements Comparator<Impiegato> {

	@Override
	public int compare(Impiegato o1, Impiegato o2) {
		// criterio che induce l'ordinamento per salario
		return o1.getDataAssunzione().compareTo(o2.getDataAssunzione());
	}

}