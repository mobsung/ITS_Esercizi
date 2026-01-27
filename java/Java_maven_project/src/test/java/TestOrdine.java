import cartoleria.Cliente;
import cartoleria.Gomma;
import cartoleria.Ordine;
import cartoleria.Penna;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class TestOrdine {

    @Mock
    Cliente cliente;

    @Mock
    Penna p1;
    @Mock
    Penna p2;
    @Mock
    Gomma g1;

    @InjectMocks
    Ordine ordine;


    @Test
    void testCalcolaTotate(){
        when(p1.getPrezzoVendita()).thenReturn(10);
        when(p2.getPrezzoVendita()).thenReturn(15);
        when(g1.getPrezzoVendita()).thenReturn(20);

        ordine.aggiungiArticolo(p1);
        ordine.aggiungiArticolo(p2);
        ordine.aggiungiArticolo(g1);

        double result = ordine.calcolaTotale();
        assertEquals(45.0, result);
    }


    @Test
    void testChiudiConto(){
        assertFalse(ordine.isPagato());
        ordine.chiudiConto();
        assertTrue(ordine.isPagato());
        verify(cliente).paga(ordine.calcolaTotale());

    }


}
