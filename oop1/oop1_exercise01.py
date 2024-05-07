class TV:
    def __init__(self, size: int) -> None:
        self.__volume: int = 50
        self.__channel: int = 1
        self.__size = size
        self.__on: bool = False
    
    def get_on(self) -> bool:
        return self.__on

    def turn_on_off(self):
        self.__on = not self.__on


    @property
    def volume(self) -> int:
        return self.__volume
    
    @volume.setter
    def volume_up(self, volume: int) -> None:
        if (self.__volume + volume) <= 99:
            self.__volume += 1
    
    @volume.setter
    def volume_down(self, volume: int) -> None:
        if (self.__volume - volume) >= 1:
            self.__volume -= 1
    

    @property
    def channel(self) -> int:
        return self.__channel

    def channel_change(self, channel: int) -> None:
        if channel <= 1 or channel >= 99:
            raise ValueError("Unavailable channel")        
        self.__channel = channel


if __name__ == "__main__":
    tv = TV(60)
    print("TV is on?", tv.get_on())
    tv.turn_on_off()
    print("TV is on?", tv.get_on())
    tv.volume_up = 40
    print("Volume: ", tv.volume)
    tv.volume_up = 20
    print("Volume: ", tv.volume)
    tv.channel_change(10)
    print("Channel: ", tv.channel)
    tv.turn_on_off()
    print("TV is on?", tv.get_on())
