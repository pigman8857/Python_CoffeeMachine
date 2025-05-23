MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

acceptable_coins = {
    "penny" : 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredient are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change}$ in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name} 😀")


def process_coins():
    """Returns the total calculated from coin inserted"""
    print("Please insert coin.")
    total = int(input("How many quarters? : ")) * acceptable_coins["quarter"]
    total += int(input("How many dimes? : ")) * acceptable_coins["dime"]
    total += int(input("How many nickles? : ")) * acceptable_coins["nickle"]
    total += int(input("How many pennies? : ")) * acceptable_coins["penny"]
    return total

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])



