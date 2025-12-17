package pila;

import java.util.LinkedList;

public class Pila <E>{

    private LinkedList<E> oggetti = new LinkedList<>();

    public void add(E ob){
        oggetti.addLast(ob);
    }

    public void remove(){
        if (!oggetti.isEmpty()){
            oggetti.removeLast();
        }
    }
}
