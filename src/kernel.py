import pcb

class Kernel():

    def __init__(self, scheduler, irq, shell, cpu, mmu):
        self.scheduler = scheduler
        self.irq = irq
        self.shell = shell
        self.cpu = cpu
        self.mmu = mmu
        self.kernelMode = False
        self.pid = 0
        self.irq.kernel = self
        self.shell.kernel = self

    def loadProgram(self, aProgram):
        #Loads a program, return baseDir of that program in the memory
        base = self.mmu.loadProgram(aProgram)

        #Builds new pcb to works with
        newPCB = pcb.PCB(self.pid, base, aProgram.length())

        #Adds new pcb to scheduler's rpq
        self.scheduler.addProcess(newPCB)

        #Increments pid for next process
        self.pid += 1

    def changeKernelMode(self):
        if self.kernelMode == False:
            self.setKernelMode(True)
        else:
            self.setKernelMode(False)

    def setKernelMode(self, boolean):
        self.kernelMode = boolean

    def isKernelMode(self):
        return self.kernelMode

