import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class TestCalcolatrice {
    private final Calcolatrice calcolatrice = new Calcolatrice();

    @Test
    void sumOK(){
        assertEquals(2, calcolatrice.somma(1, 1));
    }

    @Test
    void sumNotOK(){
        assertEquals(0, calcolatrice.somma(-1, 1));
    }

    @Test
    void divisioneOK() throws Exception{
        assertEquals(2.5, calcolatrice.dividi(10, 4));
    }

    @Test
    void divisioneZero(){
        Exception e = assertThrows(Exception.class, () -> calcolatrice.dividi(10, 0));
        assertEquals("errore divisione per zero", e.getMessage());
    }
}
