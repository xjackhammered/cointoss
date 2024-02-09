import random

def main():
    coin = ["Heads","Tails"]
    while True:
    
        choice = input("Choose Heads or Tails (Press 'x' to exit): ")
        result = coin_toss(coin)

        if choice.capitalize() == result:
            print("The computer chose {} and you chose {}.".format(result, choice))
            print("You chose correctly!")
        elif choice.upper() == "X":
            break
        elif choice.upper() != "HEADS" and choice.upper() != "TAILS":
            print("Not a valid choice!")
        else:
            print("The computer chose {} and you chose {}".format(result, choice))
            print("You chose wrong!")

def coin_toss(coin):
    
    toss = random.choice(coin)
    return toss

main()