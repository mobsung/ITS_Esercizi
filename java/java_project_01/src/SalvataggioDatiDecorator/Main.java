package SalvataggioDatiDecorator;

public class Main {
    static void main() {
        DataSource ds = new FileDataSource("aaaa");
        Criptazione c = new Criptazione(ds);

        System.out.println(c.encrypt(2));
    }
}
