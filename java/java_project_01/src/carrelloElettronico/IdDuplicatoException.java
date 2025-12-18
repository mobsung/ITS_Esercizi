package carrelloElettronico;

public class IdDuplicatoException extends RuntimeException{

    public IdDuplicatoException(){
        super();
    }

    public IdDuplicatoException(String reason){
        super(reason);
    }
}
