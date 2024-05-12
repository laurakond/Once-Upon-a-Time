# Write your code to expect a terminal of 80 characters wide and 24 rows high
import story

def game_start():
    """
    Runs the Game logo and starts the application.
    The logo was generated from https://patorjk.com/
    """

    title_logo = [r"""
  __   __ _   ___  ____    _  _  ____   __   __ _     __     ____  __  _  _  ____                      
 /  \ (  ( \ / __)(  __)  / )( \(  _ \ /  \ (  ( \   / _\   (_  _)(  )( \/ )(  __)                     
(  O )/    /( (__  ) _)   ) \/ ( ) __/(  O )/    /  /    \    )(   )( / \/ \ ) _)    _    _    _       
 \__/ \_)__) \___)(____)  \____/(__)   \__/ \_)__)  \_/\_/   (__) (__)\_)(_/(____)  (_)  (_)  (_)      
    """]

    #prints Title of the game
    for line in title_logo:
        print(line)

    #prints game introduction with options
    for line in story.game_intro:
        print(line)


#User input functions
def option_choice():
    """
    Runs every time the user has to choose
    provided options for game play.
    """
    while True:
        choice = input("Type '1' or '2' to make a choice: ")
        print(choice)
        if option_choice_validation(choice):
            print("option choice")
            break

    return choice


def user_input():
    """
    Asks user to input relevant data and stores it for in game use.
    """
    user = {}

    while True:
        user_name = input("Please enter your name: ").capitalize()
        print(user_name)
        if input_data_validation(user_name):
            print("works")
            break
    while True:    
        user_gender = input("Please enter your gender: ")
        print(user_gender)
        if input_data_validation(user_gender):
            if user_gender!="male" and user_gender!="female":
                print("Please enter 'male' or 'female'.")
            else:
                input_data_validation(user_gender)
                break
    
    user["name"] = user_name
    user["gender"] = user_gender

    return user

#data validation functions
def option_choice_validation(options):
    """
    checks that the user entry is a number
    """
    try:
        if options!= "1" and options!= "2":
            raise ValueError(
                "Please enter either 1 or 2."
            )
    except ValueError as e:
        print(
            f"Invalid input: {e}. Please try again."
        )
        return False

    return True


def input_data_validation(data):
    """
    This function ensures that user input is correct,
    and throws an error if provided data is in different
    format.
    This part of code was appropriated from Love Sandwiches project.
    """
    try:
        if data.isnumeric() or not data.isalpha():
            raise ValueError(
                f" {data}. Please use letters only to fill in the fields.")
        elif len(data) < 3 or len(data) > 10:
            raise ValueError(
                "Your entry must be between 3 to 10 characters long")
    except ValueError as e:
        print(
            f"Invalid input: {e}")
        print("Try again")
        return False

    return True


#gameplay functions
def instruction_or_game(data):
    if data == "1":
        print(game_text_generator(story.game_instructions))
    elif data == "2":
        print(game_text_generator(story.story_intro))


def game_text_generator(data):
    """
    Function that explains how to play.
    """
    
    text=""

    for line in data:
        text+=line
        #print(text)

    return text





game_start()
option = option_choice()
instruction_or_game(option)
#instruction_text = game_text_generator(story.game_instructions)
#begin_story = game_text_generator(story.story_intro)
#selection_generator(option, instruction_text, begin_story)

#print(instruction)
#user_input()

#print(test)


























#for sentence in story.intro:
#    print(sentence)

#for sentence in story.chapter1:
#    print(sentence)

#for sentence in story.chapter1_cont:
#    print(sentence)

#for sentence in story.chapter2:
#    print(sentence)

#for sentence in story.chapter2_cont:
#    print(sentence)

#for sentence in story.chapter2_cont2:
#    print(sentence)

#for sentence in story.chapter2_cont3:
#    print(sentence)


#print(story.intro)
#print(story.chapter1)
#print(story.chapter1_cont)
#print(story.chapter2)
#print(story.chapter2_cont)
#print(story.chapter2_cont2)
#print(story.chapter2_cont3)