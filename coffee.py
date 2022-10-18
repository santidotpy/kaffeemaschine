

import re


class CoffeeMachine:


    def __init__(self):
        self.coffee = 100
        self.milk = 5000
        self.sugar = 3000
        self.water = 200


    def recharge(self, coffee:int=0, milk:int=0, sugar:int=0, water:int=0):
        self.coffee += coffee
        self.milk += milk
        self.sugar += sugar
        self.water += water

    def make_coffee(self, milk=False, sugar=False):
        if not milk and not sugar:
            if self.check_ingredients():
                self.coffee -= 50
                self.water -= 100
                return True
            return False

        elif milk and not sugar:
            if self.check_ingredients() and self.milk >= 40:
                self.coffee -= 50
                self.milk -= 40
                self.water -= 60
                return True
            return False

        elif sugar and not milk:
            if self.check_ingredients() and self.sugar >= 30:
                self.coffee -= 50
                self.sugar -= 30
                self.water -= 100
                return True
            return False

        else:
            if self.check_ingredients() and self.sugar >= 30 and self.milk >= 40:
                self.coffee -= 50
                self.milk -= 40
                self.sugar -= 30
                self.water -= 60
                return True
            return False

    
    def check_ingredients(self):
        if self.coffee >= 50 and self.water >= 100:
            return True
        return False



if __name__ == '__main__':
    c = CoffeeMachine()
    print(c.check_ingredients())