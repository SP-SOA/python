inventory = {
    "coffee_beans": 1000,  # Units in grams
    "oat_milk": 500,  # Units in milliliters
    "soy_milk": 500,  # Units in milliliters
    "sugar": 750,  # Units in grams
    "water": 10000  # Units in milliliters
}

prices = {
    "espresso": 3.0,
    "cappuccino": 3.5,
    "latte": 4.0,
}

# Updated recipes to include oat and soy milk options
recipes = {
    "espresso": {"coffee_beans": 18, "water": 30, "sugar": 5},
    "cappuccino": {"coffee_beans": 18, "oat_milk": 150, "water": 30, "sugar": 5},  # Default milk is oat for simplicity
    "latte": {"coffee_beans": 18, "soy_milk": 200, "water": 30, "sugar": 5},  # Default milk is soy for simplicity
}

def display_menu():
    print("Welcome to our virtual coffee shop! Here's our menu:")
    for coffee, price in prices.items():
        print(f"- {coffee.title()}: ${price}")
    print()

def get_yes_no_input(prompt):
    response = input(prompt).lower()
    while response not in ["yes", "no"]:
        response = input("Please answer 'yes' or 'no': ").lower()
    return response == "yes"

def check_inventory(recipe, quantity):
    for ingredient, amount_needed in recipe.items():
        if inventory[ingredient] < amount_needed * quantity:
            print(f"Sorry, we don't have enough {ingredient} to fulfill your order.")
            return False
    return True

def update_inventory(recipe, quantity):
    for ingredient, amount in recipe.items():
        inventory[ingredient] -= amount * quantity

def process_payment(total_cost):
    total_received = 0.0
    while total_received < total_cost:
        payment = float(input(f"Your total is ${total_cost}. Amount due: ${total_cost - total_received}. Please enter your payment amount: "))
        total_received += payment
        if total_received < total_cost:
            print(f"Your payment is insufficient. You're still ${total_cost - total_received:.2f} short.")
    if total_received > total_cost:
        print(f"Here's your change: ${total_received - total_cost:.2f}. Thank you for your visit!")
    else:
        print("Thank you for the exact payment. Enjoy your coffee!")

def take_order():
    display_menu()
    coffee_type = input("What type of coffee would you like (Espresso, Cappuccino, Latte)? ").lower()
    
    if coffee_type not in prices:
        print("We don't offer that type of coffee. Please try again.")
        return
    
    quantity = int(input("How many coffees would you like? "))
    if not check_inventory(recipes[coffee_type], quantity):
        return
    
    milk_type = "none"
    if coffee_type != "espresso":
        milk_type = input("What type of milk would you like (Oat, Soy)? ").lower()
        if milk_type not in ["oat", "soy"]:
            print("We only offer Oat or Soy milk. Please try again.")
            return

    print(f"\nYour current order: {quantity} x {coffee_type.title()}{' with ' + milk_type.title() + ' milk' if milk_type in ['oat', 'soy'] else ''}.")
    print(f"Total cost will be: ${prices[coffee_type] * quantity:.2f}")
    
    if get_yes_no_input("Are you sure about your order (Yes/No)? "):
        process_order(coffee_type, milk_type, quantity)

def process_order(coffee_type, milk_type, quantity):
    recipe = recipes[coffee_type].copy()
    if coffee_type == "cappuccino" or coffee_type == "latte":
        if milk_type == "soy" and "oat_milk" in recipe:
            recipe["soy_milk"] = recipe.pop("oat_milk")
        elif milk_type == "oat" and "soy_milk" in recipe:
            recipe["oat_milk"] = recipe.pop("soy_milk")
    
    update_inventory(recipe, quantity)
    total_cost = prices[coffee_type] * quantity
    print(f"Your order: {quantity} x {coffee_type.title()}{' with ' + milk_type.title() + ' milk' if milk_type in ['oat', 'soy'] else ''}.")
    process_payment(total_cost)

    if get_yes_no_input("Would you like to leave a rating (Yes/No)? "):
        rating = int(input("Please rate your experience with us (1-5): "))
        print(f"Thank you for rating us a {rating}!")
    
    if get_yes_no_input("Would you like to leave a tip (Yes/No)? "):
        tip = float(input("How much would you like to tip? $"))
        print(f"Thank you for your generous tip of ${tip}!")
    else:
        print("Thank you, have a great day!")

def main():
    take_order()

if __name__ == "__main__":
    main()
