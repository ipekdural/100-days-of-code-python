from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine=MoneyMachine()
menu = Menu()
latte = MenuItem("Latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("Cappuccino", 250, 100, 24, 3.0)
espresso = MenuItem("Espresso", 50, 0, 18, 1.5)
is_on = True
while is_on:
    order_name = input(f"What would you like to order?{menu.get_items()}")
    if order_name == "off":
        is_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink=menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
