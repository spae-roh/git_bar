if __name__ == "__main__":
    class Vending_machine:
        def __init__(self, items: int, money: int) -> None:
            '''constructor items-> total items in vending machine money-> buying price of each item'''
            self.items = items
            self.money = money

        def add_items(self, items):
            self.items += items



            