package LaBanca;

import java.util.Random;

public class ThreadConto extends Thread{

    private final int numero;
    private final Banca banca;


    public ThreadConto(int numero, Banca banca) {
        this.numero = numero;
        this.banca = banca;
    }

    @Override
    public void run(){

        Random rn = new Random();
        while (true){
            try
            {
                Thread.sleep(100);
                banca.bonifico(numero, rn.nextInt(10), 500);
            } catch (IndexOutOfBoundsException | InterruptedException _) {}
        }
    }
}
