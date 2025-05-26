from typing import Self
from datetime import datetime, timedelta
import re

class CodiceAeroporto(str):

    # CodiceAeroporto tipo di dato non standard definito dalla regex [A-Z]{3} secondo lo standard Iata
    # CodiceAeroporto dato <<immutable>>

    def __new__(cls, id: str | Self) -> Self:
        if not re.fullmatch(r'[A-Z]{3}', id.upper().strip()):
            raise ValueError(f'La stringa: {id} non ripetta lo standard Iata')
        return super().__new__(cls, id.upper().strip())
    

class CodiceVolo(str):
    
    # CodiceVolo tipo di dato non standard definito dalla regex [A-Z]{2}\d{1,4}
    # CodiceVolo dato <<immutable>>

    def __new__(cls, id: str | Self) -> Self:
        if not re.fullmatch(r'[A-Z]{2}\d{1,4}', id.upper().strip()):
            raise ValueError(f'La stringa: {id} non ripetta lo standard dei codici di volo')
        return super().__new__(cls, id.upper().strip())


class IntGEZ(int):

    # IntGEZ definisce i valori imteri >= 0

    def __new__(cls, value: int | Self | str | float | bool) -> Self:
        ret: Self = int.__new__(cls, value)

        if ret < 0:
            raise ValueError(f'Il valore {value} deve essere >= 0')
        return ret

class IntG1900(int):
    
    # IntG1900 definisce i valori > 1900
    # IntG1900 dato <<immutable>>
    # Nel contesto del progetto definisce il valore dell'attributo anno fondazione Compagnia aerea 

    def __new__(cls, value: int | Self | str | float | bool) -> Self:
        ret: Self = int.__new__(cls, value)

        if ret <= 1900:
            raise ValueError(f'Il valore {value} deve essere > 1900')
        return ret
    

class TimeRange:

    def __init__(self, start: datetime, end: datetime):
        if end < start:
            raise ValueError("End time must be after start time")
        self._start = start
        self._end = end

    def getStart(self) -> datetime:
        return self._start
    
    def getEnd(self) -> datetime:
        return self._end

    def timeRange(self) -> timedelta:
        return self.getEnd() - self.getStart()

    def overlap(self, other: Self) -> bool:
        return self.getStart() <= other.getEnd() and self.getEnd() >= other.getStart()
    
        '''
                        start           end
                        |-----------------|
    start            end                  start              end 
      |---------------|                    |---------------|
        '''

    def noOverlap(self, other: Self):
        return not self.overlap(other)

    def __str__(self):
        return f"TimeRange(from {self.start} to {self.end}, duration: {self.duration()})"
    

if __name__ == '__main__':

    # Test per la classe CodiceAeroporto
    # Test positivo
    ca1: CodiceAeroporto = CodiceAeroporto('AAA')

    #test negativo
    #ca2: CodiceAeroporto = CodiceAeroporto('BB1')


    # Test per la classe CodiceVolo
    # Test positivo
    cv1: CodiceVolo = CodiceVolo('AA123')

    #test negativo
    #cv2: CodiceVolo = CodiceVolo('BBB12')


    # Test per la classe IntGEZ
    # Test positivo
    print(IntGEZ(10))
    print(IntGEZ('10'))
    print(IntGEZ(10.232))
    print(IntGEZ(True))

    #Test negativo
    # print(IntGEZ(-1))
    # print(IntGEZ('-1'))
    # print(IntGEZ(-1.23))
    # print(IntGEZ('faf'))