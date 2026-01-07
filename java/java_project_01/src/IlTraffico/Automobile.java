package IlTraffico;

import java.util.LinkedList;
import java.util.List;
import java.util.function.Predicate;

public class Automobile {

    private String marca;
    private String modello;
    private String targa;
    private boolean euro5;

    public Automobile(String marca, String modello, String targa, boolean euro5) {
        this.marca = marca;
        this.modello = modello;
        this.targa = targa;
        this.euro5 = euro5;
    }

    public String getMarca() {
        return marca;
    }

    public String getModello() {
        return modello;
    }

    public String getTarga() {
        return targa;
    }

    public boolean getEuro5(){
        return euro5;
    }

    @Override
    public String toString() {
        return "Automobile{" +
                "marca='" + marca + '\'' +
                ", modello='" + modello + '\'' +
                ", targa='" + targa + '\'' +
                ", euro5='" + euro5 + '\'' +
                '}';
    }

    public static List<Automobile> filtra(List<Automobile> automobili, Predicate<Automobile> t){
        LinkedList<Automobile> filtrata = new LinkedList<>();

        for (Automobile a : automobili) {
            if(t.test(a)) {
                filtrata.add(a);
            }
        }
        return filtrata;
    }

}
