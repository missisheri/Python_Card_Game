from random import choice


def comp_turn(comp_cards, comp_hand, comp_played):
    comp_hand = choice(comp_cards)  # put next 4 lines in a def later
    print("The computer played", comp_hand)  # hide later
    comp_index = comp_cards.index(comp_hand)
    comp_cards.pop(comp_index)
    # use append since addind a string to a list, no nest
    comp_played.append(comp_hand)
    print("Cards played by the computer so far", comp_played)  # hide later
    print("The remaining computer's cards", comp_cards)  # hide this later
    return comp_hand


def user_turn(user_cards, user_hand, user_played):
    user_index = user_cards.index(user_hand)
    user_cards.pop(user_index)
    user_played.append(user_hand)
    print("Cards played by the user so far", user_played)  # remove later
    print("User's remaining cards", user_cards)


def options():
    print("a) Continue\nb) You're lying\nc) Quit")

# Module for option 'b'


def optionb(comp_cards, comp_hand, reference, user_cards, user_played, comp_played):
    if comp_hand[-1] == reference[-1]:
        print("You've guessed it wrong!")
        # use extend, not append to avoid nested and empty lists
        user_cards.extend(user_played)
        user_cards.extend(comp_played)
        print("This is your updated list of cards: ", user_cards)
    else:
        print("You've guessed it right!")
        comp_cards.extend(comp_played)
        comp_cards.extend(user_played)
        print("Updated Computer's cards: ", comp_cards)

        """
            if comp_hand[1] == reference[1]:
                print("You've guessed it wrong!")
                user_cards.append(user_played)
                user_cards.append(comp_played)
                print("This is your updated list of cards: ", user_cards)
            else:
                print("You've guessed it right!")
                comp_cards.append(comp_played)
                comp_cards.append(user_played)
                print("Updated Computer's cards: ", comp_cards)
                """
