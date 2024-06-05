from our_station import Station # type: ignore

class Traject:
    """Object class of train routes between stations."""

    def __init__(self) -> None:
        self.connections_used: list = []
        self.time = 0

    def add(self, station1: "Station", station2: "Station", duur: int) -> None:
        self.connections_used.append([station1.name, station2.name, duur])