package PrenotazioneVoli;

public class PostiNonDispException extends Exception{

    public PostiNonDispException(){
        super();
    }

    public PostiNonDispException(String reason){
        super(reason);
    }
}
