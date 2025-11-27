from myTypes import CodiceVolo, TimeRange


class Volo:

    _codice_volo: CodiceVolo # <<immutable>>
    _duration: TimeRange

    def __init__(self, codice_volo: str | CodiceVolo, duration: TimeRange) -> None:
        self._codice_volo = CodiceVolo(codice_volo)
        self._duration = TimeRange(duration)

    def getDuration(self) -> TimeRange:
        return self._duration
        