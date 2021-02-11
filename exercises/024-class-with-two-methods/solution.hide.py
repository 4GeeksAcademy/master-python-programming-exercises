class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()