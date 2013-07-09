class IRQHandler():
    def __init__(self, irq):
        self.irq = irq
        self.irq.handler = self

    def contextSwitch(self):
        #Change to kernel, to kernel mode.
        self.irq.kernel.changeKernelMode()

        #Get current process from cpu, added to the scheduler rpq.
        current = self.irq.kernel.resourcesManager.cpu.getCurrentProcess()
        self.irq.kernel.scheduler.addProcess(current)

        #Ask for next process to the scheduler
        newProcess = self.irq.kernel.scheduler.getProcess()
        self.irq.kernel.resourcesManager.cpu.setCurrentProcess(newProcess)

        #Change kernel, to user mode again.
        self.irq.kernel.changeKernelMode()

    def contextSwitchIO(self):
        pcb = self.irq.kernel.resourcesManager.io.currentPCB
        self.irq.kernel.scheduler.addProcess(pcb)
        self.irq.kernel.resourcesManager.io.reset()

    def timeOut(self):
        self.contextSwitch()

class IRQ():
    def __init__(self):
        self.handler = None
        self.kernel = None

    def setKernel(self, aKernel):
        self.kernel = aKernel

    def setHandler(self, anIRQHandler):
        self.handler = anIRQHandler()

    def contextSwitch(self):
        self.handler.contextSwitch()

    def contextSwitchIO(self):
        self.handler.contextSwitchIO()

    def timeout(self):
        self.handler.timeOut()

