import unittest
from coffee import CoffeeMachine

class Test_Coffee_Machine(unittest.TestCase):

    def test_make_coffee(self):
        c = CoffeeMachine()
        self.assertTrue(c.make_coffee())

    def test_make_coffee_descontar_coffee_water(self):
        c = CoffeeMachine()
        c.make_coffee()
        self.assertEqual(c.coffee, 50)
        self.assertEqual(c.water, 100)
    
    def test_make_coffee_descontar_milk_sugar(self):
        c = CoffeeMachine()
        c.make_coffee(milk=True, sugar=True)
        self.assertEqual(c.coffee, 50)
        self.assertEqual(c.water, 140)
        self.assertEqual(c.milk, 4960)
        self.assertEqual(c.sugar, 2970)

    
    def test_make_latte(self):
        c = CoffeeMachine()
        self.assertTrue(c.make_coffee(milk=True))

    def test_make_sweet_coffee(self):
        c = CoffeeMachine()
        self.assertTrue(c.make_coffee(sugar=True))

    def test_make_sweet_latte(self):
        c = CoffeeMachine()
        self.assertTrue(c.make_coffee(milk=True, sugar=True))

    def test_make_latte_no_ingredients(self):
        c = CoffeeMachine()
        c.make_coffee()
        c.make_coffee()
        self.assertFalse(c.make_coffee(milk=True))

    def test_recharge_coffee(self):
        c = CoffeeMachine()
        c.recharge(coffee=100)
        cafe = c.coffee
        self.assertEqual(cafe, 200)

    def test_recharge_milk(self):
        c = CoffeeMachine()
        c.recharge(milk=100)
        leche = c.milk
        self.assertEqual(leche, 5100)

    def test_recharge_sugar(self):
        c = CoffeeMachine()
        c.recharge(sugar=100)
        azucar = c.sugar
        self.assertEqual(azucar, 3100)

    def test_check_ingredients(self):
        c = CoffeeMachine()
        c.make_coffee()
        self.assertTrue(c.check_ingredients())

    def test_check_ingredients_false(self):
        c = CoffeeMachine()
        c.make_coffee()
        c.make_coffee()
        self.assertFalse(c.check_ingredients())
    



if __name__ == '__main__':
    unittest.main()