class MMU():
    def __init__(self, anAsignation):
        self.asignation = anAsignation

    def loadProgram(self, aProgram):
        return self.asignation.loadProgram(aProgram)       

