# *************BASIC IDEA**********************************
# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# total_price_of_item1 = item1_price * item1_quantity
#
# print(type(item1))                # item1 has been instantiated from a class 'str'
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(total_price_of_item1))
# ************************************************************

# create the class
class Item :
    # functions inside classes are called methods:
    def calculate_total_price(self, x, y) :  # self --> python passes itself as the first arg when u call the method
        # from an instance
        return x * y


# creating instance of a class
item1 = Item()
# creating attributes to the instances
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))  # self --> item1, x--> item1.price, y-->item1.quantity

item2 = Item()
# creating attributes to the instances
item2.name = "Laptop"
item2.price = 200
item2.quantity = 10
print(item2.calculate_total_price(item2.price, item2.quantity))

# print(type(item1))          # of datatype --> Item
# print(type(item1.name))     # of datatype --> str
# print(type(item1.price))
# print(type(item1.quantity))
