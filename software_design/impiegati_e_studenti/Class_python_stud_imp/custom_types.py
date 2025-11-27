from typing import Self, Any
import re
from datetime import *

class CodiceVolo(str):
    # Gli oggetti di questa classe *sono* stringhe
    #  che rispettano il formato dei codici dei voli: XY1234
    def __new__(cls, cv: str) -> Self:
        cv: str = cv.upper().strip()  # rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z0-9]{2}\d{4}$', cv):
            return super().__new__(cls, cv)

        raise ValueError(f"La stringa '{cv}' non è un codice valido per un volo!")


class CodiceIATA(str):
    def __new__(cls, c: str) -> Self:
        if re.fullmatch(r'^[A-Z]{3}$', c):
            return super().__new__(cls, c)
        raise ValueError(f"La stringa '{c}' non è un codice IATA valido per un aeroporto!")



class IntGE1900(int):
    # Tipo di dato specializzato Intero >= 1900
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 1900:
            return n
        raise ValueError(f"Il valore {n} è minore di 1900!")


class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")


class IntGZ(int):
    # Tipo di dato specializzato Intero > 0 (Greater than Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n > 0:
            return n
        raise ValueError(f"Il valore {n} non è positivo!")
	

class RealGEZ(float):
    # Tipo di dato specializzato Reale >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)  # prova a convertire v in un float
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")
    

class TimeRange(tuple):	
	_start: datetime|None # [0..1]
	_end: datetime|None # [0..1]
	# subject to constraint: _start <= _end

	def __new__(cls, start:datetime|str|None, end:datetime|str|None)->Self:	
		# We accept _start == None or _end == None (unbounded time periods)

		values = [ datetime.fromisoformat(x) if isinstance(x, str) else x for x in [start, end] ]
		if values[0] and values[1] and values[0] > values[1]:
			raise ValueError(f"Invalid TimeRange(from={start}, to={end}): 'from' must be <= 'to'")
		return tuple.__new__(cls, values)

	def start(self)->datetime|None:
		return self[0]
	def end(self)->datetime|None:
		return self[1]

	def duration(self)->timedelta|None:
		try:
			return self.end() - self.start()
		except:
			return timedelta.max # we should return timedelta(+infty), but timedelta has no standard representation of +infty

	def is_disjoint(self, other:Self)->bool:

		# case #1:
		# self :        X---------------
		# other: ---X           

		# case #2:
		# self : ---------------X
		# other:                   X----

		# case #3:
		# self :        X-------X
		# other: ---X      or      X----

		if self.start(): #1, #3
			if other.end() and other.end() < self.start():
				return True #1
			
		if self.end(): #2, #3
			if other.start() and other.start() > self.end():
				return True #3

		return False

	def intersects(self, other:Self)->bool:
		return not self.is_disjoint(other)

	def shift(self, delta:timedelta)->Self:
		if not delta:
			return self
		else:
			return TimeRange(
				None if not self.start() else self.start() + delta, 
				None if not self.end() else self.end() + delta)

	def __str__(self)->str:
		return f"{ f'[{self[0]}' if self[0] else '(-infinity'}, { f'{self[1]}]' if self[1] else '+infinity)'}"
	

class Indirizzo:
	# campi dati:
	# _via:str
	# _civico:...
	def __init__(self, via:str, civico:str):
		if via is None:
			raise ValueError(f"via cannot be None")
		if civico is None:
			raise ValueError(f"civ cannot be None")
		
		self._via:str = via

		if not re.search("^[0-9]+[a-zA-Z]*$", civico):
			raise ValueError(f"value for civico '{civico}' not allowed")
		self._civico:str = civico
	
	def via(self)->str:
		return self._via
	def civico(self)->str:
		return self._civico

	def __repr__(self)->str:
		return f"Indirizzo(via={self.via()}, civico={self.civico()})"


	# class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
	def __hash__(self)->int:
		return hash( (self.via(), self.civico()) )

	def __eq__(self, other:Any)->bool:
		if other is None or \
				not isinstance(other, type(self)) or \
				hash(self) != hash(other):
			return False
		return (self.via(), self.civico() ) == (other.via(), other.civico())


class CodiceFiscale:

	pass



