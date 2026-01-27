import cartoleria.Azienda;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestClienteAzienda {

    private final Azienda clienteAzienda = new Azienda("Stefano", 200);

    @Test
    void testDenaroDisponibili() {
        assertEquals(200, clienteAzienda.getConto());
    }

    @Test
    void testPagamentoPositivo(){
        clienteAzienda.paga(100);
        assertTrue(clienteAzienda.getConto() > 0);
    }

    @Test
    void testPagamentoNegativo(){
        clienteAzienda.paga(300);
        assertFalse(clienteAzienda.getConto() > 0);
    }

}
