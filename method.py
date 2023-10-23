class fruits:
    def __init__(self, type, price, color):
        self.type=type
        self.price=price
        self.color=color
    def onyesha(self):
        print(f"I like eating {self.type} and it cost {self.price} of color {self.color}")

#creating an object
myObj=fruits("Banana", 20 ,"Yellow")
myObj2=fruits("Mangoes " , 40 , "Yellow")

myObj2.onyesha()
myObj.onyesha()

