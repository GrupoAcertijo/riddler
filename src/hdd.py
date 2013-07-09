class HDD(list):

    def readProgram(self, path):
        for program in self:
            if program.getPath() == path:
                return program

        #raise exception?

    def lenProgram(self, path):
        for program in self:
            if program.getPath() == path:
                return program.length()

    def swapPageToPCB(self, aPCB, pageNumber, instrcs):
        swappedPages = None
        for x in self:
            if(x.getPath() == aPCB):
                swappedPages = x
                break
        if swappedPages:
            swappedPages.addPages(pageNumber, instrcs)
            return

        mockProgram = MockProgram(aPCB, pageNumber, instrcs)
        self.append(mockProgram)

    def getSwappedPage(self, aPCB, pageNumber):
        swappedPage = None
        for each in self:
            if each.getPath() == aPCB:
                swappedPage = aPCB
       #if not swappedPage:
       #    raise someException()
        return swappedPage.getPageNumbers(pageNumber)

class MockProgram():
    """ Just created, to be able to save the swapped page to the pcb """
    def __init__(self, aPCB, pageNumber, instrcs):
        self.mockPath = aPCB
        self.pageNumbers = {}

    def getPath(self):
        return self.mockPath

    def getPageNumbers(self):
        return self.pageNumbers

    def addPage(self, pageNumber, instrcs):
        self.pageNumbers[pageNumber] = instrcs

    def getPage(self, pageNumber):
        return self.getPageNumbers()[pageNumber]

    def popPage(self, pageNumber):
        page = self.getPageNumbers()[pageNumber]
        del(self.getPageNumbers()[pageNumber])
        return page

