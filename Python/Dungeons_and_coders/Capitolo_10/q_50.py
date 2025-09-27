'''
Un polinomio runico deve rispondere alle concentrazioni con esattezza. Lascia che la richiesta sia parte del protocollo: `Polynomial(coeffs)` con coefficienti dal termine **costante** e `evaluate(x)` che somma `coeff[i] * x**i`. Mantieni la firma data e fai superare tutti i test automatici.
'''


class Polynomial:
    
    def __init__(self, coeffs) -> None:
        self.coeffs = coeffs

    def evaluate(self, x) -> int:

        tot = 0
        for i in range(len(self.coeffs)):
            tot += (self.coeffs[i] * x**i)
        
        return tot

p=Polynomial([1,0,2])

print(p.evaluate(3))