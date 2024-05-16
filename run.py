# Write your code to expect a terminal of 80 characters wide and 24 rows high
import story
#import os
from time import sleep

user_name = ""
user_gender = ""

def welcome_screen():
    """
    Runs the Game logo and starts the application.
    The logo was generated from https://patorjk.com/
    """

    title_logo = [r"""
  __  __ _  ___ ____    _  _ ____  __  __ _     __     ____ __ _  _ ____         
 /  \(  ( \/ __|  __)  / )( (  _ \/  \(  ( \   / _\   (_  _|  | \/ |  __)        
(  O )    ( (__ ) _)   ) \/ () __(  O )    /  /    \    )(  )(/ \/ \) _) _ _ _   
 \__/\_)__)\___|____)  \____(__)  \__/\_)__)  \_/\_/   (__)(__)_)(_(____|_|_|_)  

    """]

    #prints Title of the game
    for line in title_logo:
        print(line)

    #prints game introduction with options
    for line in story.story_dict["game_intro"]:
        print(line)


#User input functions
def option_choice():
    """
    Runs every time the user has to choose
    provided options for game play.
    """
    while True:
        choice = input("Type '1' or '2' to make a choice: ")
        #print(choice)
        if option_choice_validation(choice):
            #print("option choice")
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
            #return user_name
    while True:    
        user_gender = input("Please enter your gender: ")
        print(user_gender)
        if input_data_validation(user_gender):
            if user_gender!="male" and user_gender!="female":
                print("Please enter 'male' or 'female'.")
            else:
                input_data_validation(user_gender)
                break
                #user_gender
    
    user["name"] = user_name
    user["gender"] = user_gender
    print(user)
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


def yes_no_validation(data):
    """
    This function validates y/n input field.
    """

    try:
        if data.isnumeric() or not data.isalpha():
            raise ValueError(
                f"{data}. Please type 'y' or 'n'."
            )
        elif len(data)>1:
            raise ValueError(
                "Entry must be either 'y' or 'n'."
            )
    except ValueError as e:
        print(
            f"Invalid input {e}. Try again."
        )
        return False
    
    return True


#gameplay functions
def instruction_or_game(data):
    """
    takes the user to the instructions or
    gameplay
    """
    if data == "1":
        print(game_text_generator(story.story_dict["game_instructions"]))
        return continue_to_play(proceed_to_game())
        #print(test)
    else:
    #elif data == "2":
        user_input()
        print(game_text_generator(story.story_dict["story_intro"]))
        print(game_text_generator(story.story_dict["chapter1"]))
        return path_selector()
        #custom_name = [line.replace("{user_name}", user["name"]) for line in story.story_intro]
        #return game_text_generator(custom_name)


def proceed_to_game():
    """
    This function runs after instructions and asks if the 
    user wants to continue to play the game
    """
    while True:
        question = input("Would you like to play the game (y/n)? ").lower()
        if yes_no_validation(question):
            #print("yes no validation works")
            break
        
    return question


def continue_to_play(data):
    """
    generates appropriate game play functions based
    on user choice after reading instructions
    """
    if data =="y":
        user_input()
        print(game_text_generator(story.story_dict["story_intro"]))
        print(game_text_generator(story.story_dict["chapter1"]))
        return path_selector()
        #return chapter1
        #print(run_chapter1())
        #return run_chapter1()
        #return introduction
    elif data =="n":
        return end_game()


def end_game():
    """Generates a goodbye message"""

    bye_text = "Thanks for playing! See you next time."
    print(bye_text)
    #os.system('cls')

    
def game_text_generator(story):
    """
    Returns the text line by line for the game from the story.py.
    """    
    text=""
    for line in story:
        text+=line

    return text


#def run_chapter1():
    #chapter1 = game_text_generator(["chapter1"])
    #return chapter1


def path_selector():
    while True:
        first_question = input("Type '1' or '2' to make a choice: ")
        if option_choice_validation(first_question):
            break

    return test(first_question)
    #return chapter1





#test = run_chapter1()
#print(test)
welcome_screen()
option = option_choice()
instruction_or_game(option)
#smth = path_selector
#test(smth)
#test = proceed_to_game()
#print(test)
#continue_to_play(proceed_to_game())
#print(smth)
#introduction = game_text_generator(story.story_dict["story_intro"])
#sleep(3)
#game_text_generator(story.story_intro)
#instruction_text = game_text_generator(story.game_instructions)
#begin_story = game_text_generator(story.story_intro)
#selection_generator(option, instruction_text, begin_story)




