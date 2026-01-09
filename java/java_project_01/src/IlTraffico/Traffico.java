package IlTraffico;

import java.util.LinkedList;
import java.util.Random;

public class Traffico {

    private LinkedList<Automobile> automobili = new LinkedList<>();
    private int condizioniAria;
    public static int ordinanza;

    public Traffico() {
        condizioniAria = setCondizioniAria();
        setAutomobili();
    }

    public LinkedList<Automobile> getAutomobili() {
        return automobili;
    }

    public int getCondizioniAria() {
        return condizioniAria;
    }

    public int setCondizioniAria(){
        Random random = new Random();
        return random.nextInt(360, 1000);
    }

    private void setAutomobili(){
        Random random = new Random();

        String[] marche = {"Fiat", "BMW", "Audi", "Reno", "Peugeut", "Stefano"};
        String[] modelli = {"Panda", "Golf", "Corolla", "Focus", "Serie 3", "A4", "Classe C", "208", "Clio", "Model 3"};
        char[] alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

        int numeroAuto = random.nextInt(1,50);

        for (int i = 0; i < numeroAuto; i++){

            String marca = marche[random.nextInt(marche.length)];
            String modello = modelli[random.nextInt(modelli.length)];
            boolean euro5 = (random.nextBoolean());
            StringBuilder targa = new StringBuilder();

            for (int j = 0; j < 7; j++){
                if (j < 2 || j > 4){
                    targa.append(alphabet[random.nextInt(alphabet.length)]);
                } else {
                    targa.append(random.nextInt(9));
                }
            }

            automobili.add(new Automobile(marca, modello, targa.toString(), euro5));

        }

    }

    public boolean AriaM700(){
        return condizioniAria > 700;
    }

    public boolean autoMcosa(int thr){
        return automobili.size() > thr;
    }

    public void showAutomobili(){
        String auto = "";

        for(Automobile a: automobili){
            auto += "\n" + a.toString();
        }

        System.out.println(auto);
    }

    public static void setOrdinanza(){
       ordinanza = (ordinanza % 2 == 0) ? 1 : 0;
    }
}
