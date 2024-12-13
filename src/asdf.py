
class Item:

    def __init__(self,name,price):
        self.name = name
        self.price = price

class Cart:

    def __init__(self,name):
        self.name = name
        self.cargo = []

    def add_item(self,item):
        self.cargo.append(item)

    def sum_price(self):
        total = 0
        for item in self.cargo:
            total = total + item.price
        return total

if __name__ == "__main__":
    item_1 = Item("apple",10)
    item_2 = Item("orange",20)


    Cart_1 = Cart("Cart_1")
    Cart_1.add_item(item_1)
    Cart_1.add_item(item_2)

    for item in Cart_1.cargo:
        print(item.name)

    print(Cart_1.sum_price())