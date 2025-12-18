package carrelloElettronico;

public class IdNonPresenteException extends RuntimeException{

    public IdNonPresenteException(){
        super();
    }

    public IdNonPresenteException(String reason){
        super(reason);
    }

}
