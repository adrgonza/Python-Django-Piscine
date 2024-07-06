import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0
        self.isbroke = False

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        print("The coffee machine is broken.")
        print("Repairing the coffee machine...")
        self.drinks_served = 0
        self.isbroke = False
        print("The coffee machine has been repaired and is ready to serve drinks again.")

    def serve(self, beverage_class):
        if self.isbroke:
            raise self.BrokenMachineException()
        
        self.drinks_served += 1
        if self.drinks_served > 10:
            self.isbroke = True
            return self.EmptyCup()
        
        if random.choice([True, False]):
            return beverage_class()
        else:
            return self.EmptyCup()

if __name__ == "__main__":
    nescafe = CoffeeMachine()

    beverages_to_serve = [
        beverages.Cappuccino,
        beverages.Chocolate,
        beverages.Tea,
        beverages.Coffee,
        beverages.HotBeverage
    ]

    for beverage in beverages_to_serve:
        for i in range(7):
            try:
                print(nescafe.serve(beverage))
            except nescafe.BrokenMachineException:
                nescafe.repair()
                break
