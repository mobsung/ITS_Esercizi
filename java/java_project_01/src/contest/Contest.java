package contest;

import java.util.LinkedList;

public class Contest {

    private final LinkedList<Performer> performers = new LinkedList<>();

    public void signUp(Performer per) throws RuntimeException{
        if (!performers.contains(per)){
            performers.add(per);
        } else {
            throw new RuntimeException("Il performer esiste già");
        }
    }

    public void registerVoteFor(Performer per) throws RuntimeException{
        if (performers.contains(per)){
            per.incrementaVoto();
        } else {
            throw new RuntimeException("Il performer non esiste");
        }
    }

    public Performer getWinner(){
        Performer winner = performers.getFirst();
        for (Performer p : performers){
            winner = (winner.compareTo(p) > 0) ? winner : p;
        }
        return winner;
    }

    @Override
    public String toString() {
        return "Contest{" +
                "performers=" + performers +
                '}';
    }
}
