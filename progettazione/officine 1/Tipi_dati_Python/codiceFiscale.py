import re

class CodiceFiscale:

    pattern = re.compile(r'[A-Z]{6}[0-9]{2}[ABCDEHLMPRST]{1}[0-9]{2}([A-Z]{1}[0-9]{3})[A-Z]{1}')

    def __init__(self, cf: str):
        self._setCf(cf)

    def _setCf(self, cf: str) -> None:

        if re.fullmatch(self.pattern, cf):
            self.cf = cf
        else:
            raise ValueError('Il CF inserito non è corretto')
        
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.cf == other.cf

    def __hash__(self):

        return hash((self.cf))
        
        


if __name__ == '__main__':

    cf1 : CodiceFiscale = CodiceFiscale('MVLMCL01C14Z140O')
    cf2 : CodiceFiscale = CodiceFiscale('MVLMCL01C14Z140O')
    cf3 : CodiceFiscale = CodiceFiscale('LVMLCM01C14Z140O')

    print({cf1, cf2})