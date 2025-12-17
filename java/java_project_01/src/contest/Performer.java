package contest;


import java.util.Objects;

public class Performer implements Comparable<Performer>{

    private int voti;
    private final String nome;

    public Performer(String nome) {
        this.nome = nome;

    }

    public int getVoti() {
        return voti;
    }

    public void incrementaVoto(){
        voti += 1;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Performer performer = (Performer) o;
        return voti == performer.voti && Objects.equals(nome, performer.nome);
    }

    @Override
    public int hashCode() {
        return Objects.hash(voti, nome);
    }

    @Override
    public int compareTo(Performer p){
        if (this.getVoti() > p.getVoti()){
            return 1;
        } else if (this.getVoti() == p.getVoti()){
            return 0;
        } else {
            return -1;
        }
    }

    @Override
    public String toString() {
        return "Performer{" +
                "voti=" + voti +
                ", nome='" + nome + '\'' +
                '}';
    }
}
