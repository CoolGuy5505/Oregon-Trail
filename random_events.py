from my_coloring import *

class Event:
    def __init__(self, ch_data):
        self.broken_legs = 0
    
    def broken_leg(self, ch_data):
        if self.broken_legs < 2:
            if self.broken_legs == 0:
                print(color.warning('You have broken your right leg.'))
                ch_data['-_health_mod'] += 0.03
            if self.broken_legs == 1:
                print(color.warning('You have broken your left leg'))
                ch_data['-_health_mod'] += 0.03
            self.broken_leg += 1
        else:
            print('Your broken legs have worsened')
            ch_data['-_health_mod'] += 0.04