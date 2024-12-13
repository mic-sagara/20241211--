import pandas as pd
from src.asdf import Item, Cart  

item_1 = Item('apple',50)
item_2 = Item('orange',100)

cart_1 = Cart('sagara')
cart_1.add_item(item_1)
cart_1.add_item(item_2)
total = cart_1.sum_price()

print(total)


data = {
    "A": [10, 40, 50],
    "B": [30, 20, 60],
    "C": [20, 80, 10],
    "D": ["X", "Y", "Z"]  
}

df = pd.DataFrame(data)
print(df)