class ContinousAsignation():
    def __init__(self, memory, asignationFit):
        self.memory = memory
        self.asignationFit = asignationFit
        self.fillBlocks = []

    def loadProgram(self, aProgram):
        if aProgram.length() > self.memory.size:
            raise NotEnoughMemoryException()
        else:
            if self.getFreeSize() > aProgram.length():
                return self.asignationFit.loadProgram(aProgram, self.memory, self)

    def compact(self):
        position = 0
        for block in self.getFillBlocks():
            positionBlock = block.getBase()
            if positionBlock < block.size:
                i = self.memory.memory.index(positionBlock)
                self.memory.memory.insert(position, i)
                position += 1

    def getFreeBlocks(self):
        freeBlocks = []
        position = 0
        if self.getAmountFillBlocks() == 0:
            freeBlocks.append(Block(position, self.memory.size))
        else:
            for block in self.fillBlocks:
                freeBlocks.append(Block(position, block.getBase() - position))
                position = block.getBase() + block.size + 1
        return freeBlocks

    def getFreeSize(self):
        total = 0
        if self.getAmountFillBlocks() == 0:
            total = self.memory.getSize()
        else:
            for block in self.fillBlocks:
                total += block.size
        return total

    def getFillBlocks(self):
        return self.fillBlocks

    def getAmountFreeBlocks(self):
        return len(self.getFreeBlocks())

    def getAmountFillBlocks(self):
        return len(self.getFillBlocks())

class AsignationFit:
    def loadProgram(self, aProgram, memory, asignation):
        pass

class WorstFit(AsignationFit):
    def loadProgram(self, aProgram, memory, asignation):
        newBlock = None
        for block in asignation.getFreeBlocks():
            if newBlock == None:
                newBlock = block
            else:
                if block.size() > newBlock.size():
                    newBlock = block
        if newBlock.size >= aProgram.size:
            return memory.loadProgram(aProgram, newBlock)
        else:
            self.compact()
            self.loadProgram(aProgram, memory)

class FirstFit(AsignationFit):
    def loadProgram(self, aProgram, memory, asignation):
        for block in asignation.getFreeBlocks():
            if block.size >= aProgram.length():
                return memory.loadProgram(aProgram, block)
                break
        else:
            self.compact()
            self.loadProgram(aProgram, memory)

class BestFit(AsignationFit):
    def loadProgram(self, aProgram, memory, asignation):
        newBlock = None
        for block in asignation.getFreeBlocks():
            if newBlock == None:
                newBlock = block
            else:
                if block.size >= aProgram.size & block.size < newBlock.size:
                    newBlock = block
        if newBlock.size < aProgram.size:
            self.compact()
        else:
            return memory.loadProgram(aProgram, newBlock)

class NotEnoughMemoryException(Exception):
    def __str__(self):
        return "Not enough memory. Program size is bigger than memory size."

class Block():

    def __init__(self, aBase, aSize):

        self.base = aBase
        self.size = aSize

    def getBase(self):
        return self.base

