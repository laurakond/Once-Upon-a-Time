import gspread
from google.oauth2.service_account import Credentials
import story
from time import sleep
from os import system
# The idea of using the above system from os import and
# system("clear") module was taken from fellow student's
# Georgina Carlisle project:
# https://github.com/GeorginaCarlisle/detective-game-p3

# Gspread part of code, including imports in lines 1-2 
# was appropriated from Love Sandwiches walkthrough 
# project by Code Institute.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('once-upon-a-time')


# Main function to run the game
def main():
    """
    Main game function
    """
    welcome_screen()
    option = option_choice()
    choose_instruction_or_game(option)


def welcome_screen():
    """
    Runs the Game logo and starts the application.
    """
    # prints main logo
    generate_logos(story.ascii_dict["title_logo"])

    # prints game introduction with options
    generate_game_text(1)


# User input functions
def option_choice():
    """
    Runs every time the user has to choose
    provided options for game play.
    """
    while True:
        choice = input("\nType '1' or '2' to proceed: ")
        if option_choice_validation(choice):
            break

    return choice


def user_input():
    """
    Asks user to input relevant data and stores it for in game use.
    """
    while True:
        user_name = input("\nPlease enter your name: ").capitalize()
        if input_data_validation(user_name):
            break
    while True:
        user_gender = input("Please enter your gender: ")
        if input_data_validation(user_gender):
            if user_gender != "male" and user_gender != "female":
                print("Please enter 'male' or 'female'.")
            else:
                input_data_validation(user_gender)
                break

    story.user["name"] = user_name
    story.user["gender"] = user_gender
    return story.user


def proceed_to_game(prompt):
    """
    This function runs after instructions and asks if the
    user wants to continue to play the game.
    """
    while True:
        question = input(prompt).lower()
        if yes_no_validation(question):
            break

    return question


# data validation functions
def option_choice_validation(options):
    """
    Checks that the user entry is a number.
    """
    try:
        if options != "1" and options != "2":
            raise ValueError(
                "Please enter either 1 or 2"
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
        if data != "y" and data !="n":
            raise ValueError(
                "Please type either 'y' or 'n'"
            )
    except ValueError as e:
        print(
            f"Invalid input: {e}. Please try again."
        )
        return False

    return True
    

# Text/storyline generating functions
def generate_logos(logo):
    """
    Prints ascii art
    """
    for line in logo:
        print(line)


def customise_story(story_text, user_name):
    """
    Customises the storyline based on user provided data,
    for example, name and (gender - future feature).
    """
    updated_story = []
    for line in story_text:
        updated_line = line.replace("{user_name}", user_name)
        updated_story.append(updated_line)

    return updated_story


def game_text_generator(story):
    """
    Returns the text line by line for the game from the story.py.
    """
    text = ""
    for line in story:
        text += line

    return text


# This function replaced game_text_generator(story)
# which was used when the story text was stored in 
# story.py
def generate_game_text(column_number):
    """
    Retrieves story text from imported gspread
    and returns it line by line for the user 
    to read.
    Replaces user data(name/gender) by passing 
    customise_story() function.
    """
    text = SHEET.worksheet("story")
    generated_text = text.col_values(column_number)[1:]

    customized_text = customise_story(generated_text, story.user["name"])
    for line in customized_text:
        print(line)


# Gameplay functions
def choose_instruction_or_game(data):
    """
    Takes the user to the instructions or
    gameplay.
    """
    if data == "1":
        system("clear")
        # prints instruction logo
        generate_logos(story.ascii_dict["instructions"])
        generate_game_text(2)
        sleep(3)
        return continue_to_play(proceed_to_game(
                                "Would you like to play the game (y/n)? "))
    elif data == "2":
        user_input()
        system("clear")
        generate_logos(story.ascii_dict["title_logo"])
        #new_story = customise_story(story.story_dict["story_intro"],
        #                            story.user["name"])
        #generated_text = game_text_generator(new_story)
        #print(generated_text)
        generate_game_text(3)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        #print(game_text_generator(story.story_dict["chapter1"]))
        generate_game_text(4)
        return execute_chapter1(option_choice())


def continue_to_play(data):
    """
    Generates appropriate game play functions based
    on user choice after reading instructions.
    """
    if data == "y":
        user_input()
        system("clear")
        generate_logos(story.ascii_dict["title_logo"])
        #new_story = customise_story(story.story_dict["story_intro"],
         #                           story.user["name"])
        #generated_text = game_text_generator(new_story)
        #print(generated_text)
        generate_game_text(3)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        #print(game_text_generator(story.story_dict["chapter1"]))
        generate_game_text(4)
        return execute_chapter1(option_choice())
    elif data == "n":
        return end_game()


def end_game():
    """
    Generates a goodbye message.
    """
    bye_text = "\nThanks for playing! See you next time."
    print(bye_text)
    

def restart_game(main_function):
    """
    Restarts the gameplay & takes the user
    to the beginning of the application.
    """
    sleep(10)
    system("clear")
    return main_function()


def execute_chapter1(data):
    """
    Generates appropriate game play based on option selection.
    """
    if data == "1":
        sleep(3)
        #print(game_text_generator(story.story_dict["confront_queen"]))
        generate_game_text(5)
        return restart_game(main)
    elif data == "2":
        sleep(3)
        generate_game_text(6)
        #print(game_text_generator(story.story_dict["rumpel"]))
        return execute_rumpel_section(option_choice())


def execute_rumpel_section(data):
    """
    Returns appropriate result after chapter1 continued.
    """
    if data == "1":
        sleep(3)
        generate_logos(story.ascii_dict["chapter2"])
        #print(game_text_generator(story.story_dict["chapter2"]))
        generate_game_text(8)
        return execute_baby_name_section(option_choice())
    if data == "2":
        sleep(3)
        generate_game_text(7)
        #print(game_text_generator(story.story_dict["no_name"]))
        return restart_game(main)


def execute_baby_name_section(data):
    """
    Returns appropriate result after chapter2.
    """
    if data == "1":
        sleep(3)
        generate_game_text(9)
        #print(game_text_generator(story.story_dict["fight_army"]))
        return restart_game(main)
    if data == "2":
        sleep(3)
        generate_game_text(10)
        #print(game_text_generator(story.story_dict["secret_door"]))
        return execute_secret_door_section(option_choice())


def execute_secret_door_section(data):
    """
    Returns appropriate result after secret door section.
    """
    if data == "1":
        sleep(3)
        generate_game_text(11)
        #print(game_text_generator(story.story_dict["fight_soldier"]))
        return restart_game(main)
    if data == "2":
        sleep(3)
        generate_game_text(12)
        #print(game_text_generator(story.story_dict["lock_door"]))
        return execute_lock_door_section(option_choice())


def execute_lock_door_section(data):
    """
    Returns appropriate result after locked door section.
    """
    if data == "1":
        print("\nSuccess!")
        sleep(3)
        #wardrobe_story = customise_story(story.story_dict["wardrobe"],
         #                                story.user["name"])
        #wardrobe_text = game_text_generator(wardrobe_story)
        #print(wardrobe_text)
        generate_game_text(13)
        return continue_to_chapter3()
    if data == "2":
        sleep(3)
        generate_game_text(11)
        #print(game_text_generator(story.story_dict["fight_soldier"]))
        return restart_game(main)


def continue_to_chapter3():
    """
    Takes the user to Chapter 3 or executes end_game()
    based on user input.
    """
    question = proceed_to_game(
               "Would you like to continue to Chapter 3 (y/n)? ")
    if question == "y":
        print("\nComing soon - stay tuned, Deary!")
        return end_game()
    elif question == "n":
        return end_game()


# Reused variables
#instructions = game_text_generator(story.story_dict["game_instructions"])

# Runs the game:
main()
