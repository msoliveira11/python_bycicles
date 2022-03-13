from bicicleta import Bycicle

class Gravel(Bycicle):

    def __init__(self):
        Bycicle.__init__(self,"Gravel")
        self.setDesc("Bicicleta hibrida.")

