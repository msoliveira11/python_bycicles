from bicicleta import Bycicle

class MTB(Bycicle):

    def __init__(self):
        Bycicle.__init__(self,"MTB")
        self.setDesc("Bicicleta de trilha.")
