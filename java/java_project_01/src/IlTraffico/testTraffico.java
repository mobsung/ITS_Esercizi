package IlTraffico;


import java.util.LinkedList;
import java.util.List;

public class testTraffico {
    static void main() {

        Traffico traffico = new Traffico();
        List<Automobile> filtrate = traffico.getAutomobili();
        //traffico.showAutomobili();
        System.out.println(traffico.getCondizioniAria());

        //List<Automobile> filtroPari = Automobile.filtra(automobili, a -> a.getTarga().charAt(a.getTarga().length() - 3) % 2 == 0);
        if (traffico.AriaM700()){
            filtrate = Automobile.filtra(filtrate, a -> a.getEuro5());
        }

        if (traffico.autoMcosa(30) || Traffico.ordinanza % 2 == 0){
            filtrate = Automobile.filtra(filtrate, a -> a.getTarga().charAt(a.getTarga().length() - 3) % 2 != 0);
            Traffico.setOrdinanza();
        } else if(traffico.autoMcosa(30)){
            filtrate = Automobile.filtra(filtrate, a -> a.getTarga().charAt(a.getTarga().length() - 3) % 2 == 0);
            Traffico.setOrdinanza();
        }

        filtrate.forEach(f -> System.out.println(f));
    }
}
