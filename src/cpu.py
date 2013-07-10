class CPU():

    def __init__(self, aIRQ, anIO, aMMU):
        self.currentProcess = None
        self.irq = aIRQ
        self.io = anIO
        self.mmu = aMMU

    def execute(self):
    #This method needs to be modified with the next steps:
    # if currentProcess not == None, ask mmu for nextInstruction
    # if the instruction is a cpu one, execute it; if not sends it to IO
        """ Executes next instruction of current process """
        if self.currentProcess == None:
            self.irq.contextSwitch()
        elif self.currentProcess.hasNextInstruction(self.currentProcess.size):
            currentProcessPC = self.currentProcess.getPc()
            instructionToExec = self.mmu.getNextInstruction(self.currentProcess)
            if not instructionToExec == None:
                self.dispatchToExecute(instructionToExec)
        else:
            self.irq.contextSwitch()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

    def getCurrentProcess(self):
        return self.currentProcess

    def dispatchToExecute(self, anIntruction):
        anInstruction.determineDispatching(self)
   
    def dispatchToIOExecution(self):
        self.io.addPCB(self.currentProcess)
        self.setCurrentProcess(None)

