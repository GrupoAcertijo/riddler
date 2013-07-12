class CPU():

    def __init__(self, aIRQ, anIO, aMMU):
        self.currentProcess = None
        self.irq = aIRQ
        self.io = anIO
        self.mmu = aMMU

    def execute(self):
        """ Executes next instruction of current process """
        if self.currentProcess == None:
            self.irq.handler.firstProcess()
        elif self.currentProcess.hasNextInstruction(self.currentProcess.getSize()):
            currentProcessPC = self.currentProcess.getPc()
            instructionToExec = self.mmu.getNextInstruction(self.getCurrentProcess())
            if not instructionToExec == None:
                self.dispatchToExecute(instructionToExec)
        else:
            self.irq.contextSwitch()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

    def getCurrentProcess(self):
        return self.currentProcess

    def dispatchToExecute(self, anInstruction):
        anInstruction.determineDispatching(self)
   
    def dispatchToIOExecution(self):
        self.io.addPCB(self.currentProcess)
        self.setCurrentProcess(None)

