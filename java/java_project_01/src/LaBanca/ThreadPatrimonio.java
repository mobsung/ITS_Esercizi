package LaBanca;

public class ThreadPatrimonio extends Thread{

    private final Banca banca;

    public ThreadPatrimonio(Banca banca) {
        this.banca = banca;
    }

    public void run(){
        while (true){
            System.out.println(banca.getPatrimonio());
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
