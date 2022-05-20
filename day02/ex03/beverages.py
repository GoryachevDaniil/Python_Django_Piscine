class HotBeverage(object):
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40
        
    def description(HotBeverage):
            return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(HotBeverage):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(HotBeverage):
        return "Un po' di Italia nella sua tazza!"

