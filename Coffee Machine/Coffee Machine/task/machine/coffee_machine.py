def main():
    coffee_cups()


def stock():
    water = int(input('Write how many ml of water the coffee machine has:'))
    milk = int(input('Write how many ml of milk the coffee machine has:'))
    coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has:'))
    return water, milk, coffee_beans


def coffee_cups():
    water, milk, coffee_beans = stock()
    cups = int(input('Write how many cups of coffee you will need:'))
    can_make = min(water // 200, milk // 50, coffee_beans // 15)
    if can_make == cups:
        print('Yes, I can make that amount of coffee')
    elif can_make < cups:
        print(f'No, I can make only {can_make} cups of coffee')
    else:
        print(f'Yes, I can make that amount of coffee (and even {can_make - cups} more than that)')


main()
