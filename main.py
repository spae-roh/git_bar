if __name__ == "__main__":
    class Vending_machine:
        def __init__(self, items: int, money: int) -> None:
            '''constructor items-> total items in vending machine money-> buying price of each item'''
            self.items = items
            self.money = money
        
    cola = Vending_machine(10, 20)
    print(cola.items, cola.money)


            