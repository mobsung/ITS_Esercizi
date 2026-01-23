
import tamagotchi.Tamagotchi;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class TestTamagotchi {

    private final Tamagotchi tama = new Tamagotchi("Real", "GATTO");

    @Test
    void testTipi(){
        assertEquals("Real", tama.getNome());
        assertEquals(tamagotchi.Tamagotchi.Specie.GATTO, tama.getSpecie());
        assertEquals(10, tama.getAltezza());
        assertEquals(100, tama.getPeso());
        assertEquals(3, tama.getEnergia());
    }

    @Test
    void testMangia(){
        assertTrue(tama.mangia());
        assertEquals(11, tama.getAltezza());
        assertEquals(250, tama.getPeso());
        assertEquals(4, tama.getEnergia());
    }

    @Test
    void testGiocaEnergiaZero(){
        tama.mangia();
        tama.mangia();
        tama.mangia();
        tama.gioca();
        tama.gioca();
        tama.gioca();
        tama.gioca();
        tama.gioca();
        assertEquals(1, tama.getEnergia());
        assertFalse(tama.gioca());
        assertEquals(1, tama.getEnergia());
    }

    @Test
    void testGiocaPesoMinimo(){
        assertFalse(tama.gioca());
        assertTrue(tama.getPeso() > 0);
    }

    @Test
    void testIntegrativo(){
        assertTrue(tama.mangia());
        assertTrue(tama.dorme());
        assertTrue(tama.gioca());
        assertEquals(100 + 150 - 100, tama.getPeso());
        assertEquals(10 + 1, tama.getAltezza());
        assertEquals(3 + 1 + 1 - 1, tama.getEnergia());

    }

}
