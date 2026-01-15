package LaBanca;

public class testBanca {

    static void main() {

    Banca b1 = new Banca();

    Thread t0 = new ThreadConto(0, b1);
    Thread t1 = new ThreadConto(1, b1);
    Thread t2 = new ThreadConto(2, b1);
    Thread t3 = new ThreadConto(3, b1);
    Thread t4 = new ThreadConto(4, b1);
    Thread t5 = new ThreadConto(5, b1);
    Thread t6 = new ThreadConto(6, b1);
    Thread t7 = new ThreadConto(7, b1);
    Thread t8 = new ThreadConto(8, b1);
    Thread t9 = new ThreadConto(9, b1);

    Thread tPatrimonio = new ThreadPatrimonio(b1);

    t0.start();
    t1.start();
    t2.start();
    t3.start();
    t4.start();
    t5.start();
    t6.start();
    t7.start();
    t8.start();
    t9.start();

    tPatrimonio.start();

    }



}
