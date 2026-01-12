package EsercizioAdapter;

public class testPayment {
    static void main() {
        PaymentSystem p0 = new PaymentSystem();
        PaymentAdapterSol1 p1 = new PaymentAdapterSol1(p0);
        PaymentAdapterSol2 p2 = new PaymentAdapterSol2();

        p1.pay(23);
        p2.pay(22);
    }
}
