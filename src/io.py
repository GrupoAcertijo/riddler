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
            self.irq.contextSwitchIO()

    def reset(self):
        self.currentPCB = None

    def getCurrentPCB(self):
        return self.currentPCB

