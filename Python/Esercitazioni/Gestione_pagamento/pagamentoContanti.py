'''
Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.
'''

from pagamento import Pagamento

class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()

    def dettagliPagamento(self) -> None:
        print(f'Importo del pagamento: €{round(self.getImporto(), 2)} in contanti!')

    def inPezziDa(self) -> None:
        str_pezzi_da: str = ''
        importo = self.getImporto()

        tagli_banconote: list[float] = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.01]

        while importo > 0:
            if importo // tagli_banconote[0] > 0:
                if importo // 5 > 0:
                    str_pezzi_da += f'{int(importo // tagli_banconote[0])} banconote da {tagli_banconote[0]} euro\n'

                else:
                    str_pezzi_da += f'{int(importo // tagli_banconote[0])} monete da {tagli_banconote[0]} euro\n'

            importo = round(importo % tagli_banconote[0], 2)

            tagli_banconote.pop(0)
        print(str_pezzi_da)


if __name__ == '__main__':

    pagamento1: PagamentoContanti = PagamentoContanti()
    pagamento1.setImporto(999.99)

    pagamento1.inPezziDa()