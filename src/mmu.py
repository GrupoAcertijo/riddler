class MMU():

    def __init__(self, anAsignation):
        self.asignation = anAsignation

    def loadProgram(self, aProgram):
        return self.asignation.loadProgram(aProgram)       

    def getNextInstruction(self, aPCB):
        return self.asignation.getNextInstruction(aPCB)
    
    def getFreeSize(self):
        return self.asignation.getFreeSize()

