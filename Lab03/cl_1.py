class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getstring(self):
        self.input_string = input("Enter a string: ")

    def printstring(self):
        print("String in upper case: ", self.input_string.upper())
        

