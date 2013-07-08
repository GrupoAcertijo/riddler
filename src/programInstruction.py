class Program():

    def __init__(self, aName=None, aPath=None):
        self.name = aName
        self.path = aPath
        self.instructions = []

    def length(self):
        return len(self.getInstructions())

    def getPath(self):
        return self.path

    def add(self, aInstruction):
        self.instructions.append(aInstruction)

    def setInstructions(self, instrcs):
        self.instructions = instrcs

    def getInstructions(self):
        return self.instructions

    def getInstruction(self, i):
        return self.instructions[i]

class Instruction():

    def execute(self):
        pass

class CPUInstruction(Instruction):
    def isIO(self):
        return False

    def execute(self):
        print "CPU Instruction"

class IOInstruction(Instruction):

    def isIO(self):
        return True

    def execute(self):
        print "IO Instruction"

class EndInstruction(Instruction):
    def isIO(self):
        return False

    def execute(self):
        print "END Instruction"

