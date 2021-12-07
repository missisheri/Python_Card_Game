from random import shuffle, choice, randint
from lcg_modules import user_turn, comp_turn, options, optionb

# CREATE PACKAGES FOR THE MODULES, SEPARATE MODULES

cards = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
         "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
         "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
         "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
comp_cards = []  # set of computer's cards
user_cards = []  # set of users cards
comp_hand = ""  # last card played by comp, can be a variable instead
user_hand = ""
comp_played = []  # set of cards played by comp
user_played = []

reference = choice(cards)
reference_index = cards.index(reference)
print("This is the reference card:", reference)
cards.pop(reference_index)
print("\n", cards)  # remove later
shuffle(cards)
print("\n", cards)  # remove later
comp_cards = cards[0:25]
user_cards = cards[25:50]
print("\nThe computer's cards are:", comp_cards)  # hide this later
print("\nYour cards are:", user_cards)

comp_num = randint(1, 10)
user_num = randint(1, 10)
if comp_num > user_num:  # the player with the highest number plays first
    print("\nComputer's turn to play")
    # keep playing until no cards or (add user quits)
    while comp_cards and user_cards:
        comp_hand = comp_turn(comp_cards, comp_hand, comp_played)
        # add following code to when user starts playing first
        options()
        option = input("Choose between options a, b, and c: ").lower()
        if option == "a":
            print("Let's keep playing")
        elif option == "b":
            print("reference", reference)
            print("comp_hand", comp_hand)
            optionb(comp_cards, comp_hand, reference,
                    user_cards, user_played, comp_played)
            # how to get rid of the empty list and nested list in the updated list after append
        elif option == "c":
            print("Goodbye!")
            break
        print("\nIt's your turn to play")
        user_hand = input("Enter the card you would like to play: ").upper()
        if user_hand in user_cards:
            user_turn(user_cards, user_hand, user_played)
        else:
            print("The card you picked does not exist in your list of card")
            continue
        print("\nComputer's turn to play")
        comp_turn(comp_cards, comp_hand, comp_played)
    else:
        if not comp_cards:
            print("The computer won!")
        elif not user_cards:
            print("You're the winner!")
elif user_num >= comp_num:
    # keep playing unless no cards or(add user quits)
    while comp_cards and user_cards:
        print("\nIt's your turn to play")
        user_hand = input("Enter the card you would like to play: ").upper()
        if user_hand in user_cards:
            user_turn(user_cards, user_hand, user_played)
        else:
            print("The card you picked does not exist in your list of card")
            continue
        print("\nComputer's turn to play")
        comp_turn(comp_cards, comp_hand, comp_played)
    if not comp_cards:
        print("The computer won!")
    elif not user_cards:
        print("You're the winner!")
