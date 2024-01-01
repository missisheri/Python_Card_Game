from random import choice

def comp_turn(comp_cards: list, comp_played: list) -> str:
    """
    Computer's turn in the Liar Card Game.
    
    Args:
    comp_cards (list): List of the computer's remaining cards.
    comp_played (list): List of cards played by the computer.
    
    Returns:
    str: The card played by the computer.
    """
    comp_hand = choice(comp_cards)
    comp_cards.remove(comp_hand)
    comp_played.append(comp_hand)
    
    # Uncomment these print statements to debug.
    # print("The computer played", comp_hand)
    # print("Cards played by the computer so far", comp_played)
    # print("The remaining computer's cards", comp_cards)
    
    return comp_hand

def user_turn(user_cards: list, user_hand: str, user_played: list) -> None:
    """
    Function for the user's turn in the Liar Card Game.
    
    Args:
    user_cards (list): List of the user's remaining cards.
    user_hand (str): The card played by the user.
    user_played (list): List of cards played by the user.
    """
    user_cards.remove(user_hand)
    user_played.append(user_hand)
    
    # Uncomment these print statements to debug.
    # print("Cards played by the user so far", user_played)
    # print("User's remaining cards", user_cards)

def options():
    """
    Prints the options available to the user during their turn.
    """
    print("a) Continue\nb) You're lying\nc) Quit")

def optionb(comp_cards: list, 
            comp_hand: str, 
            reference: str, 
            user_cards: list, 
            user_played: list, 
            comp_played: list) -> None:
    """
    Function to handle the scenario where the user accuses the computer of lying.
    
    Args:
    comp_cards (list): List of the computer's cards.
    comp_hand (str): The last card played by the computer.
    reference (str): The reference card.
    user_cards (list): List of the user's cards.
    user_played (list): Cards played by the user.
    comp_played (list): Cards played by the computer.
    """
    if comp_hand[-1] == reference[-1]:
        print("You've guessed it wrong!")
        user_cards.extend(user_played + comp_played)
        print("This is your updated list of cards: ", user_cards)
    else:
        print("You've guessed it right!")
        comp_cards.extend(user_played + comp_played)
        print("Updated Computer's cards: ", comp_cards)
