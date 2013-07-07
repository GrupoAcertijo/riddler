class IRQ():
    def __init__(self, handler, kernel):
        self.handler = handler
        self.kernel = kernel

class IRQHandler():
    def __init__(self, irq):
        self.irq = irq

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
        pcb = self.irq.io.currentProcess
        self.kernel.scheduler.addProcess(pcb)
        self.irq.io.reset()

    def timeout(self):
        self.contextSwitch()
