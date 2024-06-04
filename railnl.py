from station import Station

class Railnl:
    def __init__(self) -> None:
        self.stations: dict[str, "Station"] = {}
    
    def load_stations(self) -> None:
        with open("data/StationsHolland.csv") as f:
                    for line in f:
                        if line == "\n":
                            break
                        name, x, y = line.strip().split(',')
                        station = Station(name, x, y)
                        self.stations[name] = station
        print(self.stations)


    def load_connections(self) -> None:
        with open("data/ConnectiesHolland.csv") as f:
                    for line in f:
                        if line == "\n":
                            break
                        station1, station2, afstand = line.strip().split(',')
                        self.stations[station1].add_connection(self.stations[station2], afstand)
                        self.stations[station2].add_connection(self.stations[station1], afstand)

    def max_connections(self) -> int:
        print(self.stations.keys())
        return max(self.stations[station].number_of_connections() for station in self.stations.keys())


if __name__ == "__main__":
    railnl = Railnl()
    railnl.load_connections()
    railnl.load_stations()
    print(railnl.max_connections())
            
          

    