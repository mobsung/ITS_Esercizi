package TestStringa;


import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class EsempiStringa {
    private static final Logger logger= LogManager.getLogger(EsempiStringa.class);

    public static void main(String[] args) {
        EsempiStringa es=new EsempiStringa();
        int oc=es.contaOccorrenze("Lorem ipsum test prova Roberto","r");

        logger.info("log4j Funzione e le occorrenza {}", oc);
        System.out.println(oc);
    }
    public boolean isPalindroma(String str1) {
        String str2 = "";

        for(int i = str1.length()-1; i >= 0; i--) {
            str2 += str1.charAt(i);
        }

        return str1.equals(str2);
    }

    public int contaOccorrenze(String testo, String carattere) {
        int count = 0;
        for (int i = 0; i < testo.length(); i++) {
            if (String.valueOf(testo.charAt(i)).equals(carattere)) {
                count++;
            }
        }
        return count;
    }
}
