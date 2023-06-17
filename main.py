if __name__ == "__main__":
    class Vending_machine:
        '''vending machine code'''

        def __init__(self, items: int, money: int) -> None:
            '''constructor items-> total items in vending machine money-> buying price of each item'''
            self.items = items
            self.money = money

        def add_items(self, items):
            if self.items+items <= 100:
                self.items += items
            else:
                print("request container of items cannot be added. limited space left is ",(100-self.items))


print("check1 added")
print("check2 added")            