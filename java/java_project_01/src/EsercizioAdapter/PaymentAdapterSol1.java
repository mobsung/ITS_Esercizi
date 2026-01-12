package EsercizioAdapter;

public class PaymentAdapterSol1 implements PaymentProcessor{
    public PaymentSystem paymentSystem;

    public PaymentAdapterSol1(PaymentSystem paymentSystem) {
        this.paymentSystem = paymentSystem;
    }

    @Override
    public void pay(double amount) {
        paymentSystem.makePayment((int)amount);
    }
}
