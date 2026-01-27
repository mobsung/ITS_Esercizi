import cartoleria.Privato;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestClientePrivato {

    private final Privato clientePrivato = new Privato("Stefano", 200);

    @Test
    void testDenaroDisponibili() {
        assertEquals(200, clientePrivato.getDenaro());
    }

    @Test
    void testPagamentoPositivo(){
        clientePrivato.paga(100);
        assertTrue(clientePrivato.getDenaro() > 0);
    }

    @Test
    void testPagamentoNegativo(){
        clientePrivato.paga(300);
        assertFalse(clientePrivato.getDenaro() > 0);
    }
}
