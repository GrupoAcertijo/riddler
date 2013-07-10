import clock

class IO():

    def __init__(self, anIRQ, aMMU):
        self.readyQueue = []
        self.currentPCB = None
        self.irq = anIRQ
        self.mmu = aMMU

    def addPCB(self, aPCB):
        self.readyQueue.append(aPCB)

    def execute(self):
        if self.currentPCB == None and not (len(self.readyQueue) == 0):
            self.readyQueue.reverse()
            self.currentPCB = self.readyQueue.pop()
            self.readyQueue.reverse()

            i = self.mmu.getNextInstruction(self.currentPCB)
            i.execute()
            self.currentPCB.incPc()
           #Aca se podria hacer una comprobacion de si la proxima 
           #instruccion tambien es de IO, para no hacer 
           #un contextSwitching innecesario, o en su defecto varios...
           #porque podria ocurrir que las 
           #proximas 3 instrucciones sean de IO 
            self.irq.contextSwitchIO()

    def reset(self):
        self.currentPCB = None

    def getCurrentPCB(self):
        return self.currentPCB

