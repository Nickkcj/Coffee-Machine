from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


order = input("What drink do you want? (espresso/latte/vanilla): ")
while order != "off":
    if order == "report":
        coffee_maker.report()
    item = menu.find_drink(order)
    if item:
        if coffee_maker.is_resource_sufficient(item):
            for drink in menu.menu:
                if drink.name == order:
                    cost = drink.cost
                    
            money_machine.make_payment(cost)
            coffee_maker.make_coffee(item)
            order = input("What drink do you want? (espresso/latte/vanilla): ")

