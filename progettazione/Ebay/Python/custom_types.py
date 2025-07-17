import re
from typing import Self

class Url(str):

    pattern = re.compile (r"^https?://[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(/[a-zA-Z0-9\-_./]*)?$")
    
    def __init__(self, url):
        if not self.isValid(url):
            raise ValueError ("Invalid URL")
        self.url = url
        
    @classmethod   
    def isValid(cls,url:str)->bool:
        return bool(cls.pattern.fullmatch(url))
    
class RealGZ(float):

    # RealGZ definisce i valori reali > 0
    
    def __new__(cls, value: float | int | str | bool | Self) -> Self:
        ret: Self = float.__new__(cls, value) 

        if ret < 0:
            raise ValueError (f"The value {value} must be > 0")
        return ret
    
class IntGEZ(int):

    # IntGEZ definisce i valori imteri >= 0

    def __new__(cls, value: int | Self | str | float | bool) -> Self:
        ret: Self = int.__new__(cls, value)

        if ret < 0:
            raise ValueError(f'Il valore {value} deve essere >= 0')
        return ret