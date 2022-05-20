from beverages import *
import random 

class CoffeeMachine(object):
    def __init__(self):
        self.counter = 10

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "hot beverage"
            self.price = 0.30

        def description(HotBeverage):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.counter = 10

    def serve(self, elem):
        if self.counter == 0:
            raise self.BrokenMachineException
        self.counter -= 1
        return random.choice([elem, self.EmptyCup()])

def machine():
    machine = CoffeeMachine()
    cof = Coffee()
    tea = Tea()
    choc = Chocolate()
    capp = Cappuccino()
    for i in range(1, 12):
        try:
            machine.serve(random.choice([cof, tea, choc, capp]))
            print(f"Cup {i} complete.")
        except machine.BrokenMachineException as exc:
            print(exc)
            machine.repair()
    try:
        machine.serve(random.choice([cof, tea, choc, capp]))
        print(f"One more cup complete.")
    except machine.BrokenMachineException as exc:
        print(exc)
        machine.repair()

if __name__ == '__main__':
    machine()