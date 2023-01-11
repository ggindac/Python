
""" Chapter 8 Ex. 2
Write a program that simulates a television by creating it as an object. The user should be able to enter
a channel number and raise or lower the volume. Make sure that the channel number and volume level
stay within valid ranges. """


class Television(object):
    """Television simulation"""
    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume

    def raise_volume(self):
        self.volume += 1
        if self.volume > 10:
            self.volume = 10
        print("\nVolume ", self.volume)

    def lower_volume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print("\nVolume ", self.volume)

    def switch_channel_up(self):
        self.channel += 1
        if self.channel > 99:
            self.channel = 0
        print("\nChannel ", self.channel)

    def switch_channel_down(self):
        self.channel -= 1
        if self.channel < 0:
            self.channel = 99
        print("\nChannel ", self.channel)

    def specify_channel(self):
        self.channel = int(input("\nChoose channel ---> "))
        print("Channel ", self.channel)


def main():
    tv = Television()
    option = -1

    while option != 0:
        print("""
                1. Raise volume
                2. Lower volume
                3. Switch channel - up
                4. Switch channel - down
                5. Specify channel
                0. Exit
        """)
        option = int(input("---> "))

        if option == 1:
            tv.raise_volume()
        if option == 2:
            tv.lower_volume()
        if option == 3:
            tv.switch_channel_up()
        if option == 4:
            tv.switch_channel_down()
        if option == 5:
            tv.specify_channel()


main()
input("\nPress enter...")
