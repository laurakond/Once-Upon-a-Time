import gspread
from google.oauth2.service_account import Credentials
import story
from time import sleep
from os import system
# The idea of using the above from os import system and
# system("clear") module was taken from a fellow student
# Georgina Carlisle's project:
# https://github.com/GeorginaCarlisle/detective-game-p3

# Gspread part of the code, including imports in lines 1-2,
# was appropriated from the Love Sandwiches walkthrough
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

# Reused variables
WELCOME_SCREEN_INTRO_TEXT_COLUMN = 1
GAME_INSTRUCTION_TEXT_COLUMN = 2
STORY_INTRODUCTION_TEXT_COLUMN = 3
CHAPTER_ONE_TEXT_COLUMN = 4
CONFRONT_QUEEN_OUTCOME_TEXT_COLUMN = 5
RUMPEL_SECTION_TEXT_COLUMN = 6
NO_NAME_OUTCOME_TEXT_COLUMN = 7
CHAPTER_TWO_TEXT_COLUMN = 8
FIGHT_ARMY_OUTCOME_TEXT_COLUMN = 9
SECRET_DOOR_SECTION_TEXT_COLUMN = 10
FIGHT_SOLDIER_OUTCOME_TEXT_COLUMN = 11
LOCK_DOOR_TEXT_COLUMN = 12
WARDROBE_TEXT_COLUMN = 13


# Main function to run the game
def main():
    """
    Main game function displayed upon loading.
    """
    welcome_screen()
    number_choice = enter_numerical_choice()
    choose_instruction_or_game(number_choice)


def welcome_screen():
    """
    Runs the Game logo and displays
    the game introduction text.
    """
    # prints main logo
    generate_logos(story.ascii_dict["title_logo"])

    # prints game introduction with options
    generate_game_text(WELCOME_SCREEN_INTRO_TEXT_COLUMN)


# User input functions
def enter_numerical_choice():
    """
    Prompts a question where the user chooses to input
    numerical values for the game to proceed.
    """
    while True:
        choice = input("\nType '1' or '2' to proceed: ")
        option_list = ["1", "2"]
        message = "'1' or '2'."
        if validate_exact_phrase_prompt(choice, option_list, message):
            break

    return choice


def input_user_data():
    """
    Asks the user to input their name/gender, validates the
    input and stores them for later in-game use.
    The gender data input is not used at the MVP stage.
    It will implemented properly at the next development stage.
    """
    while True:
        user_name = input("\nPlease enter your name: ").capitalize()
        if validate_user_input_data(user_name):
            break
    while True:
        user_gender = input(
                      "Please enter your gender(male/female/none): ").lower()
        option_list = ["male", "female", "none"]
        prompt = "'male' or 'female' or 'none'."
        if validate_exact_phrase_prompt(user_gender, option_list, prompt):
            break

    story.user["name"] = user_name
    story.user["gender"] = user_gender
    return story.user


def prompt_yes_no_question(prompt):
    """
    Generates appropriate question based on the gameplay that
    requires the user to enter yes/no answer and keeps looping
    if the input is incorrect.
    """
    while True:
        question = input(prompt).lower()
        option_list = ["y", "n"]
        message = "'y' or 'n'."
        if validate_exact_phrase_prompt(question, option_list, message):
            break

    return question


# data validation functions
def validate_user_input_data(data):
    """
    Checks that the user data input is correct,
    and throws an error if the provided data is in different
    format than it should be.
    This part of code was appropriated from Love Sandwiches project.
    The concept was also applied to other validation functions in
    this project.
    """
    try:
        if data.isnumeric() or not data.isalpha():
            raise ValueError(
                f"{data}. Please use letters only to fill in the fields.")
        elif len(data) < 3 or len(data) > 10:
            raise ValueError(
                f"{len(data)}."
                "Your entry must be between 3 to 10 characters long.")
    except ValueError as e:
        print(f"Invalid input: {e} Try again.")
        return False

    return True


def validate_exact_phrase_prompt(user_entry, option_list, error_prompt):
    """
    Checks that the input data is correct and prompts the user
    to enter the correct data if not.
    """
    try:
        if user_entry not in option_list:
            raise ValueError(
                f"{user_entry}. Please type either {error_prompt}")
    except ValueError as e:
        print(f"Invalid input: {e} Try again.")
        return False

    return True


# Text/storyline generating functions
def generate_logos(logo):
    """
    Prints ascii art.
    """
    for line in logo:
        print(line)


def customise_story(story_text, user_name):
    """
    Loops through original text and replaces specific words with
    user provided data, i.e. name & gender (future feature), and
    returns a new text to display in the terminal.
    """
    updated_story_text_list = []
    for line in story_text:
        updated_line = line.replace("{user_name}", user_name)
        updated_story_text_list.append(updated_line)

    return updated_story_text_list


# This function replaced game_text_generator(story)
# which was used when the text content was stored in
# story.py
def generate_game_text(column_number):
    """
    Retrieves story text from imported gspread
    and returns it line by line for the user
    to read.
    Replaces user data(name/gender) inside the text by passing
    customise_story() function.
    """
    text = SHEET.worksheet("story")
    generated_text = text.col_values(column_number)[1:]

    customised_text = customise_story(generated_text, story.user["name"])
    for line in customised_text:
        print(line)


def generate_line_breaks():
    """
    Prints blank lines and a separator line for
    the user to better see/follow the story progression.
    """
    print("")
    print("     ---------------------------------     ")
    print("")


# Gameplay functions
def choose_instruction_or_game(user_entry):
    """
    Takes the user to the instructions or
    the gameplay sections.
    """
    if user_entry == "1":
        system("clear")
        generate_logos(story.ascii_dict["instructions"])
        generate_game_text(GAME_INSTRUCTION_TEXT_COLUMN)
        sleep(3)
        return continue_to_play(prompt_yes_no_question(
                                "\nWould you like to play the game (y/n)? "))
    elif user_entry == "2":
        input_user_data()
        system("clear")
        generate_logos(story.ascii_dict["title_logo"])
        generate_game_text(STORY_INTRODUCTION_TEXT_COLUMN)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        generate_game_text(CHAPTER_ONE_TEXT_COLUMN)
        return execute_chapter1(enter_numerical_choice())


def continue_to_play(user_entry):
    """
    Terminates the application or continues with the gameplay based
    on the user's choice after reading the instructions.
    """
    if user_entry == "y":
        input_user_data()
        system("clear")
        generate_logos(story.ascii_dict["title_logo"])
        generate_game_text(STORY_INTRODUCTION_TEXT_COLUMN)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        generate_game_text(CHAPTER_ONE_TEXT_COLUMN)
        return execute_chapter1(enter_numerical_choice())
    elif user_entry == "n":
        return end_game()


def end_game():
    """
    Generates a goodbye message.
    """
    bye_text = "\nThanks for playing! See you next time."
    print(bye_text)


def restart_game(pass_main_function):
    """
    Restarts the gameplay and takes the user
    to the beginning of the application (main()).
    """
    sleep(10)
    system("clear")
    return pass_main_function()


def execute_chapter1(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_line_breaks()
        generate_game_text(CONFRONT_QUEEN_OUTCOME_TEXT_COLUMN)
        return restart_game(main)
    elif user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(RUMPEL_SECTION_TEXT_COLUMN)
        return execute_rumpel_section(enter_numerical_choice())


def execute_rumpel_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_logos(story.ascii_dict["chapter2"])
        generate_game_text(CHAPTER_TWO_TEXT_COLUMN)
        return execute_baby_name_section(enter_numerical_choice())
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(NO_NAME_OUTCOME_TEXT_COLUMN)
        return restart_game(main)


def execute_baby_name_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_line_breaks()
        generate_game_text(FIGHT_ARMY_OUTCOME_TEXT_COLUMN)
        return restart_game(main)
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(SECRET_DOOR_SECTION_TEXT_COLUMN)
        return execute_secret_door_section(enter_numerical_choice())


def execute_secret_door_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_line_breaks()
        generate_game_text(FIGHT_SOLDIER_OUTCOME_TEXT_COLUMN)
        return restart_game(main)
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(LOCK_DOOR_TEXT_COLUMN)
        return execute_lock_door_section(enter_numerical_choice())


def execute_lock_door_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        print("\nSuccess!")
        sleep(3)
        generate_line_breaks()
        generate_game_text(WARDROBE_TEXT_COLUMN)
        return continue_to_chapter3()
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(FIGHT_SOLDIER_OUTCOME_TEXT_COLUMN)
        return restart_game(main)


def continue_to_chapter3():
    """
    Takes the user to Chapter 3 or executes the end_game()
    function based on the user input.
    """
    question = prompt_yes_no_question(
               "\nWould you like to continue to Chapter 3 (y/n)? ")
    if question == "y":
        print("\nComing soon - stay tuned, Deary!")
        return end_game()
    elif question == "n":
        return end_game()


# Runs the game:
main()
