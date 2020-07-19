class Menu:
    def __init__(self, options: list):
        self.options = options
    
    def printMenu(self):
        print(' [ Main Menu ] ')
        for i in range(len(self.options)):
            print((i + 1), '::', self.options[i])
    
    def createMenu(self):
        self.printMenu()
        selection = input('\nSelect Option >> ')
        return int(selection) - 1