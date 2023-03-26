import csv


# create the class
class Item:
    # creating an ALL attribute where we can initialise all 5 instances
    all = []

    pay_rate = 0.8  # this is a CLASS attribute, pay rate after 20% discount

    # functions inside classes are called methods:
    def __init__(self, name: str, price: float, quantity=0) :
        # python by default will call this method when instances are created i.e., item1,item2
        # to stop negative numbers i.e validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self) :  # self --> python passes itself as the first arg when u call the method
        # from an instance
        return self.price * self.quantity

    def discount(self) :
        self.price = self.price * self.pay_rate

    # representing objects, control to display obj when printing at console
    def __repr__(self) :
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

    @classmethod  # @--> decorator
    def instantiate_from_csv(cls) :  # --> convert this to a class method, class obj itself is passed as arg
        with open('items.csv', 'r') as f :  # read the csv file nd instantiate some objects
            reader = csv.DictReader(f)  # read our content as a list of dictionary
            items = list(reader)  # convert to a list

        for item in items :
            # create instances
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):     # not send obj as first argument
        if isinstance(num, float): # check if a floating number
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int): return True
        else: return False


# creating instance of a class
item1 = Item("Phone", 100, 1)  # --> adding INSTANCE attributes here
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# *******************************PRINT STATEMENTS********************************************
print(Item.is_integer(7.0))

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.pay_rate)
# # it will try to find the attribute in the instance level, if not present, they search class level
# print(item1.pay_rate)
# print(item2.pay_rate)
#
# # *****************MAGIC ATTRIBUTE****************************
# print(Item.__dict__)  # all attributes for CLass level
# print(item1.__dict__)  # all attributes for instance level
#
# item1.discount()
# print(item1.price)
#
# item2.pay_rate = 0.7
# item2.discount()
# print(item2.price)
