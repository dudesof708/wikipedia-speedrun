class Menu:
    def __init__(self, options: list):
        self.options = options
    
    def printMenu(self):
        print(' [ Main Menu ] ')
        for i in range(len(self.options)):
            print((i + 1), '::', self.options[i])
    
    def getMenuInput(self, waitValidated: bool):
        returnValue = -2
        while returnValue == -2:
            selection = input('Select Option >> ')
            if selection.isnumeric():
                selection = int(selection)
                if selection > 0 and selection <= len(self.options):
                    returnValue = selection - 1
            elif waitValidated:
                print('\r')
            else:
                returnValue = -1
        return returnValue

    # waitValidated waits for a valid input before returning
    def createMenu(self, waitValidated = False):
        self.printMenu()
        selection = self.getMenuInput(waitValidated)
