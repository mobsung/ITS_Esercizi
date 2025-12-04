package LasVegas;

import java.util.ArrayList;
import java.util.Scanner;

public class LasVegas {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		Dado d1 = new Dado();

		Casino c1 = new Casino("Las Vegas", 10000);

		String sceltaC = "";

		ArrayList<Giocatore> giocatori = new ArrayList<Giocatore>();

		while (!sceltaC.equalsIgnoreCase("termina")) {
			System.out.println(
					  "1 - Digita | aggiungi | per aggiungere un giocatore\n"
					+ "2 - Digita | gioca    | per avviare il gioco\n" + 
					  "3 - Digita | termina  | per terminare il gioco");

			sceltaC = sc.next();

			switch (sceltaC) {
			case "aggiungi":
				System.out.println("Indica il tuo nome ed il tuo budget iniziale per iniziare a giocare");

				System.out.print("Nome ==> ");
				String nome = sc.next();

				System.out.print("Budget ==> ");
				int budget = sc.nextInt();

				giocatori.add(new Giocatore(nome, budget));
				break;

			case "gioca":
				
				giocatori.forEach((g) -> {
					
					String scelta = "";
					int puntata = 0;
					int numero = 0;
					int importo = 0;
					
					while (!scelta.equalsIgnoreCase("termina")) {

						System.out.println(g);
						System.out.println(
								  "1 - Se vuoi depositare, digita                               | deposita      |\n"
								+ "2 - Se vuoi puntare digita                                   | punta         |\n"
								+ "3 - Se vuoi resettare la puntata ed il numero puntato digita | reset         |\n"
								+ "4 - Se vuoi resettare solo la puntata digita                 | reset puntata |\n"
								+ "5 - Se non vuoi giocare digita                               | termina       |"
								);
						scelta = sc.next();

						
						switch (scelta) {
						case "deposita":
							System.out.println("Quando vuoi depositare ==> ");
							while (importo <= 0) {
								importo = sc.nextInt();
								g.ricaricaBudget(importo);
							}
							break;

						case "punta":
							System.out.println("Quanto vuoi puntare ==> ");
							while (puntata <= 0) {
								puntata = sc.nextInt();
								if (puntata <= 0) {
									System.out.println("Devi puntare un numero un importo positivo");
								}
							}
							System.out.println("Quale numero vuoi puntare (1/6)");
							while (numero <= 0 || numero > 6) {
								numero = sc.nextInt();
								if (numero <= 0 || numero > 6) {
									System.out.println("Devi selezionare un numer ocompreso tra 1 e 6");
								}
							}
							g.punta(puntata, numero);
							break;
							
						case "reset":
							System.out.println("La punta ed in numero sono stati resettati");
							g.reset();
							break;
							
						case "reset puntata":
							System.out.println("La puntata è stata resettata");
							g.recuperaPuntata();
							break;
						}

					}
				});
				
				ArrayList<Integer> puntateVincenti = new ArrayList<Integer>();
				int dadoVincente = Dado.estrai();
				
				giocatori.forEach((g) -> {
					if (g.getPuntata() > 0 && g.getNumeroGiocato() == dadoVincente) {
						puntateVincenti.add(g.getPuntata());
					}
				});
				
				int[] puntateArray = new int[puntateVincenti.size()];
				
				if (c1.valutaPuntate(puntateArray)) {
					System.out.println("Dado vincente: " + dadoVincente);
					
					giocatori.forEach((g) -> {
						if (g.getPuntata() > 0 && g.getNumeroGiocato() == dadoVincente) {
							g.incassa();
							c1.paga(g.getPuntata());
							System.out.println("Il giocatore: " + g.getNome() + " ha puntato " + g.getPuntata() + " ed ha vinto " + (g.getPuntata() * Dado.getRICARICO()) + " monete");
							g.reset();
						} else if (g.getPuntata() > 0) {
							c1.incasso(g.getPuntata());
							System.out.println("Il giocatore: " + g.getNome() + " ha puntato " + g.getPuntata() + " ed ha perso ");
							g.reset();
						}
					});
				} else {
					System.out.println("Giocata non possibile per insufficienza di fondi");
				}
				
				break;
				

			}
		}

	}
}
