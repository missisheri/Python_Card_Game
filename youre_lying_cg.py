from random import shuffle, choice, randint
from lcg_modules import user_turn, comp_turn, options, optionb

cards = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
         "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
         "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
         "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]

comp_cards, user_cards = [], []
comp_played, user_played = [], []

reference = choice(cards)
cards.remove(reference)

# Uncomment these print statements to debug.
# print("This is the reference card:", reference)
# print("\n", cards)
shuffle(cards)
comp_cards, user_cards = cards[:25], cards[25:]

# Uncomment these print statements to debug.
# print("\nThe computer's cards are:", comp_cards)
# print("\nYour cards are:", user_cards)

comp_num, user_num = randint(1, 10), randint(1, 10)
turn = "comp" if comp_num > user_num else "user"

while comp_cards and user_cards:
    if turn == "comp":
        print("\nComputer's turn to play")
        comp_hand = comp_turn(comp_cards, comp_played)
        turn = "user"
    else:
        print("\nIt's your turn to play")
        user_hand = input("Enter the card you would like to play: ").upper()
        if user_hand in user_cards:
            user_turn(user_cards, user_hand, user_played)
            options()
            option = input("Choose between options a, b, and c: ").lower()
            if option == "a":
                print("Let's keep playing")
            elif option == "b":
                optionb(comp_cards, comp_hand, reference, user_cards, user_played, comp_played)
            elif option == "c":
                print("Goodbye!")
                break
            turn = "comp"
        else:
            print("The card you picked does not exist in your list of cards")

if not comp_cards:
    print("You're the winner!")
elif not user_cards:
    print("The computer won!")
