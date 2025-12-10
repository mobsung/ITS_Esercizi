package banca;

import java.util.Date;

public class Saving extends Standard {

	private int interesse;
	private int massimoPrelievi;

	public Saving(String intestatario, int numero, int interesse, int massimoPrelievi) {
		super(intestatario, numero);
		this.interesse = interesse;
		this.massimoPrelievi = massimoPrelievi;
	}

	public Saving(String intestatario, int numero, double saldo, int interesse, int massimoPrelievi) {
		super(intestatario, numero, saldo);
		this.interesse = interesse;
		this.massimoPrelievi = massimoPrelievi;
	}

	@Override
	public void movimento(String tipoMovimento, double ammontare, Date data) {

		if (!(tipoMovimento.equalsIgnoreCase("prelievo") && checkBalance(ammontare))) {
			System.out.println("Non hai sufficiente saldo per prelevare");
		} else {
			int counter = 0;

			for (Movimento m : getMovimenti()) {
				if (m.getData().getDay() == new Date().getDay()) {
					counter += 1;
				}
			}

			if (counter < massimoPrelievi) {

				Movimento movimento = new Movimento(tipoMovimento, data, ammontare);
				getMovimenti().add(movimento);
			} else {
				System.out.println("Hai raggiunto il limite di prelievi giornalieri");
			}

		}
	}
	
	public void calcolaInteresse() {
		setSaldo(getSaldo() * (1 + interesse / 100));
	}

}
