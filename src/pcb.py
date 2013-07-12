class PCB():

    def __init__(self, aPid, aBase, aSize):
        self.pid = aPid
        self.pc = 0
        self.base = aBase
        self.size = aSize

    def getSize(self):
        return self.size

    def size(self):
        return self.size

    def getPc(self):
        return self.pc

    def incPc(self):
        """"Increases the pc by 1"""
        self.pc += 1

    def getID(self):
        return self.pid

    def getBase(self):
        return self.base

    def hasNextInstruction(self, aSize):
        return (self.pc < aSize) and (self.pc != aSize)

class PCBPriority(PCB):

    def __init__(self, aPid, aBase, aPriority):
        PCB.__init__(self, aPid, aBase)
        self.priority = aPriority

