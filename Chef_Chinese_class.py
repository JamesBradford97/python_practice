from Chef_class import Chef

class ChineseChef(Chef): #This class inherits the Chef class

    def make_special_dish(self): #Overiding a function from the Chef class
        print("The chef makes special grilled fish")
        # return super().make_special_dish()
    def make_fried_rice(self):
        print("The chef makes fried rice")