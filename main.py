#thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#x = thistuple.index(8)
#print(x)

shopping_list = [123, 123, 444, 432, 221, 444]
store_inventory = {123: ("Tea", 4.99), 444: ("Coffee", 16.99), 432: ("Juice", 3.99), 221: ("Aero Bar", 1.19), }
total_cost = 0

for i in shopping_list:
    item_name, item_price = store_inventory[i]
    #print(item_name, item_price)
    #print("{} {}".format(item_name, item_price))
    #with formatting:
    print("{0:20s}${1:.2f}".format(item_name, item_price))
    total_cost += item_price
print("="*30)
print("{0:20s}${1:.2f}".format("TOTAL", total_cost))