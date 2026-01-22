package SalvataggioDatiDecorator;

import java.util.LinkedList;

public class Criptazione extends DataSourceDecorator{

    public Criptazione(DataSource dataSource) {
        super(dataSource);
    }

    public StringBuilder encrypt(int key){
        LinkedList<Character> alphabet = new LinkedList<>();
        for (int i = 0; i < 26; i++) {
            alphabet.add((char) ('a' + i));
        }

        StringBuilder encryped = new StringBuilder();
        String data = getDataSource().readData();

        for (int i = 0; i < data.length(); i++){
            int newIndex = (alphabet.indexOf(data.charAt(i)) + key) % 26;
            encryped.append(alphabet.get(newIndex));
        }

        return encryped;

    }
}
