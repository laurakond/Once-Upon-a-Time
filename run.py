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
    generate_game_text(1)


# User input functions
def enter_numerical_choice():
    """
    Prompts a question where the user chooses to input
    numerical values for the game to proceed.
    """
    while True:
        choice = input("\nType '1' or '2' to proceed: ")
        if validate_enter_numerical_choice(choice):
            break

    return choice


def input_user_data():
    """
    Asks the user to input their name/gender and stores them
    for later in-game use.
    """
    while True:
        user_name = input("\nPlease enter your name: ").capitalize()
        if validate_user_input_data(user_name):
            break
    while True:
        user_gender = input("Please enter your gender(male/female/none): ")
        if validate_user_input_data(user_gender):
            if user_gender not in ["male", "female", "none"]:
                print("Please enter 'male' or 'female' or 'none'.")
            else:
                validate_user_input_data(user_gender)
                break

    story.user["name"] = user_name
    story.user["gender"] = user_gender
    return story.user


def prompt_yes_no_question(prompt):
    """
    Generates appropriate question based on the gameplay that
    requires the user to enter yes/no answer.
    """
    while True:
        question = input(prompt).lower()
        if validate_yes_no_question_prompt(question):
            break

    return question


# data validation functions
def validate_enter_numerical_choice(number_choice):
    """
    Checks that the user entry is a number.
    """
    try:
        if number_choice not in ["1", "2"]:
            raise ValueError(
                f"{number_choice}. Please enter either '1' or '2'."
            )
    except ValueError as e:
        print(
            f"Invalid input: {e} Try again."
        )
        return False

    return True


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
        print(
            f"Invalid input: {e} Try again.")
        return False

    return True


def validate_yes_no_question_prompt(user_entry):
    """
    Checks that the input data is correct and prompts the user
    to enter the correct data if not.
    """
    try:
        if user_entry not in ["y", "n"]:
            raise ValueError(
                f"{user_entry}. Please type either 'y' or 'n'."
            )
    except ValueError as e:
        print(
            f"Invalid input: {e} Try again."
        )
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
        generate_game_text(2)
        sleep(3)
        return continue_to_play(prompt_yes_no_question(
                                "\nWould you like to play the game (y/n)? "))
    elif user_entry == "2":
        input_user_data()
        system("clear")
        generate_logos(story.ascii_dict["title_logo"])
        generate_game_text(3)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        generate_game_text(4)
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
        generate_game_text(3)
        sleep(10)
        generate_logos(story.ascii_dict["chapter1"])
        generate_game_text(4)
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
        generate_game_text(5)
        return restart_game(main)
    elif user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(6)
        return execute_rumpel_section(enter_numerical_choice())


def execute_rumpel_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_logos(story.ascii_dict["chapter2"])
        generate_game_text(8)
        return execute_baby_name_section(enter_numerical_choice())
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(7)
        return restart_game(main)


def execute_baby_name_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_line_breaks()
        generate_game_text(9)
        return restart_game(main)
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(10)
        return execute_secret_door_section(enter_numerical_choice())


def execute_secret_door_section(user_entry):
    """
    Generates an appropriate story section based on the user's
    gameplay selection.
    """
    if user_entry == "1":
        sleep(3)
        generate_line_breaks()
        generate_game_text(11)
        return restart_game(main)
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(12)
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
        generate_game_text(13)
        return continue_to_chapter3()
    if user_entry == "2":
        sleep(3)
        generate_line_breaks()
        generate_game_text(11)
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
