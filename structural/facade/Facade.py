from typing import Union

class PartyHall:
    
    def __init__(self) -> None:
        pass

    def schedule(self) -> bool:
        pass

class RockBand:

    def __init__(self) -> None:
        pass

    def play(self) -> None:
        pass

class Buffet:

    def __init__(self) -> None:
        pass

    def serve(self) -> None:
        pass

class Floriculture:

    def __init__(self) -> None:
        pass

    def deliver_flowers(self) -> None:
        pass

    def arrange_flowers(self) -> None:
        pass

class EventManagement:
    
    def __init__(self) -> None:
        self.party_hall = PartyHall()
        self.rock_band = RockBand()
        self.buffet = Buffet()
        self.floriculture = Floriculture()
    
    def organize(self) -> None:
        
        self.party_hall.schedule()

        self.rock_band.play()

        self.buffet.serve()

        self.floriculture.deliver_flowers()
        self.floriculture.arrange_flowers()

if __name__ == "__main__":

    eventManagement = EventManagement()
    eventManagement.organize()
