class Instrument:
    def play(self):
        return f"This instrument makes a sound."
    
class Piano(Instrument):
    def play(self):
        return f"Piano plays a melody."
    
class Drum(Instrument):
    def play(self):
        return f"Drum makes a beat."
    
class Guitar(Instrument):
    def play(self):
        return f"Guitar strums a chord."
    
def perform(instrument):
    print(instrument.play())

perform(Piano())
perform(Drum())
perform(Guitar())