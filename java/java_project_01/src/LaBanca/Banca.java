package LaBanca;

import java.util.LinkedList;
import java.util.Objects;

public class Banca {

    private static class CC {
        private int saldo;
        private final int numeroConto;

        public CC(int saldo, int numeroConto) {
            this.saldo = saldo;
            this.numeroConto = numeroConto;
        }

        public int getSaldo() {
            return saldo;
        }

        public int getNumeroConto() {
            return numeroConto;
        }

        public void aumentaSaldo(int saldo) {
            this.saldo += saldo;
        }

        public void diminuisciSaldo(int saldo) {
            this.saldo -= saldo;
        }

        @Override
        public boolean equals(Object o) {
            if (o == null || getClass() != o.getClass()) return false;
            CC cc = (CC) o;
            return numeroConto == cc.numeroConto;
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(numeroConto);
        }
    }

    private LinkedList<CC> conti = new LinkedList<>();

    public Banca() {
        for (int i = 0; i < 10; i++){
            conti.add(new CC(5000, i));
        }
    }

    public void bonifico(int ccOrdinante, int ccBeneficiario, int importo){
        for (CC cc : conti){
            if (cc.getNumeroConto() == ccOrdinante){
                for (CC ccb : conti){
                    if (ccb.getNumeroConto() == ccBeneficiario){
                        cc.diminuisciSaldo(importo);
                        ccb.aumentaSaldo(importo);
                    }
                }
            }
        }
    }

}
