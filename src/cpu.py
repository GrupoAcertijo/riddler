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
        if not self.kernel.isKernelMode():
            if self.currentProcess == None:
                self.irq.contextSwitch()
            elif self.currentProcess.hasNextInstruction(self.currentProcess.size):
                currentProcessPC = self.currentProcess.getPc()
                instructionToExec = self.kernel.resourcesManager.getNextInstruction(self.currentProcess)
                if not instructionToExec == None:
                    instructionToExec.execute()
                    self.currentProcess.incPc()
            else:
                self.irq.contextSwitch()
        else:
            self.kernel.shell.run()

    def setCurrentProcess(self, aProcess):
        self.currentProcess = aProcess

    def getCurrentProcess(self):
        return self.currentProcess

