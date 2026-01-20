package SalvataggioDatiDecorator;

public class Criptazione extends DataSourceDecorator{

    public Criptazione(DataSource dataSource) {
        super(dataSource);
    }

    public void encrypt(String data){
        char[] alphabet = new char[26];
        for (int i = 0; i < 26; i++) {
            alphabet[i] = (char) ('a' + i);
        }
        

    }
}
