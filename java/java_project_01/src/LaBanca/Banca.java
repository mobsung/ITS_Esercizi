package LaBanca;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Objects;
import java.util.stream.Collectors;

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

    public synchronized void bonifico(int ccOrdinante, int ccBeneficiario, int importo){
        HashMap<Integer, CC> nConti = new HashMap<>();
        nConti =
                (HashMap<Integer, CC>) conti.stream()
                        .collect(Collectors.toMap(
                                cc -> cc.getNumeroConto(),
                                cc -> cc
                        ));
        if (nConti.containsKey(ccOrdinante) && nConti.containsKey(ccBeneficiario)){
            if (nConti.get(ccOrdinante).getSaldo() - importo >= 0 && ccOrdinante != ccBeneficiario){
                nConti.get(ccOrdinante).diminuisciSaldo(importo);
                nConti.get(ccBeneficiario).aumentaSaldo(importo);
            }
        }
    }

    public synchronized int getPatrimonio(){
        return conti.stream()
                .map(c -> c.getSaldo())
                .reduce(0, (a, b) -> a + b);
    }


}
