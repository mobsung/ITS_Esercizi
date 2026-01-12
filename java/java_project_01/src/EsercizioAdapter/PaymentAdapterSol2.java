package EsercizioAdapter;

public class PaymentAdapterSol2 extends PaymentSystem implements PaymentProcessor {

    @Override
    public void pay(double amount) {
        makePayment((int)amount);
    }
}