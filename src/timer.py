class Timer():

    def __init__(self, anIO, aCPU, aQuantum):
        self.io = anIO
        self.cpu = aCPU
        self.quantum = aQuantum
        self.acc = 0

    def clock(self):
        if self.cpu.canExecute():
            if self.acc < self.quantum:
                self.acc += 1
                self.cpu.execute()
                self.io.execute()
            else:
                self.cpu.irq.contextSwitch()
                self.acc = 0

