package TestStringa;


import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;


class EsempiStringatest {

    //	void test() {
    //	fail("Not yet implemented");
    //	}
    @Test
    void testContaOccorrenze() {
        EsempiStringa es=new EsempiStringa();
        String testo="Roberto sta facendo java con cloud";
        int occ=5;
        assertEquals(occ,es.contaOccorrenze(testo,"o"),"Il numero di occorrenze atteso");
    }

    @Test
    void testIsPalindroma() {
        EsempiStringa es=new EsempiStringa();
        String testo="ossoro";
        //	int occ=5;
        assertTrue(es.isPalindroma(testo),"Palindroma attesa");
    }

}
