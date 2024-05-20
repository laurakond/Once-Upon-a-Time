import story
from time import sleep
from os import system
# The idea of using the above system from os import and
# system("clear") module was taken from fellow student's
# Georgina Carlisle project:
# https://github.com/GeorginaCarlisle/detective-game-p3


# Main function to run the game
def main():
    """
    Main game function
    """
    welcome_screen()
    option = option_choice()
    instruction_or_game(option)


def welcome_screen():
    """
    Runs the Game logo and starts the application.
    """

    # prints main logo
    logos(story.ascii_dict["title_logo"])

    # prints game introduction with options
    for line in story.story_dict["game_intro"]:
        print(line)


# User input functions
def option_choice():
    """
    Runs every time the user has to choose
    provided options for game play.
    """
    while True:
        choice = input("Type '1' or '2' to proceed: ")
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
    checks that the user entry is a number.
    """
    try:
        if options != "1" and options != "2":
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
        elif len(data) > 1:
            raise ValueError(
                "Entry must be either 'y' or 'n'."
            )
    except ValueError as e:
        print(
            f"Invalid input {e}. Try again."
        )
        return False

    return True


# Text/storyline generating functions
def logos(logo):
    """
    prints ascii art
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


# Gameplay functions
def instruction_or_game(data):
    """
    takes the user to the instructions or
    gameplay.
    """
    if data == "1":
        system("clear")
        # prints instruction logo
        logos(story.ascii_dict["instructions"])
        print(instructions)
        sleep(3)
        return continue_to_play(proceed_to_game(
                                "Would you like to play the game (y/n)? "))
    elif data == "2":
        user_input()
        system("clear")
        logos(story.ascii_dict["title_logo"])
        new_story = customise_story(story.story_dict["story_intro"],
                                    story.user["name"])
        generated_text = game_text_generator(new_story)
        print(generated_text)
        sleep(5)
        system("clear")
        logos(story.ascii_dict["chapter1"])
        print(game_text_generator(story.story_dict["chapter1"]))
        return chapter1(option_choice())


def continue_to_play(data):
    """
    generates appropriate game play functions based
    on user choice after reading instructions.
    """
    if data == "y":
        user_input()
        system("clear")
        logos(story.ascii_dict["title_logo"])
        new_story = customise_story(story.story_dict["story_intro"],
                                    story.user["name"])
        generated_text = game_text_generator(new_story)
        print(generated_text)
        sleep(5)
        system("clear")
        logos(story.ascii_dict["chapter1"])
        print(game_text_generator(story.story_dict["chapter1"]))
        return chapter1(option_choice())
    elif data == "n":
        return end_game(main)


def end_game(main_function):
    """Generates a goodbye message and
    returns the user to the welcome screen.
    """
    bye_text = "\nThanks for playing! See you next time."
    print(bye_text)
    sleep(5)
    system("clear")
    main_function()


def chapter1(data):
    """
    generates appropriate game play based on option selection.
    """
    if data == "1":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["confront_queen"]))
        return end_game(main)
    elif data == "2":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["rumpel"]))
        return rumpel(option_choice())


def rumpel(data):
    """
    returns appropriate result after chapter1 continued.
    """
    if data == "1":
        sleep(3)
        system("clear")
        logos(story.ascii_dict["chapter2"])
        print(game_text_generator(story.story_dict["chapter2"]))
        return baby_name(option_choice())
    if data == "2":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["no_name"]))
        return end_game(main)


def baby_name(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["fight_army"]))
        return end_game(main)
    if data == "2":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["secret_door"]))
        return secret_door(option_choice())


def secret_door(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        sleep(3)
        # system("clear")
        print(game_text_generator(story.story_dict["fight_soldier"]))
        return end_game(main)
    if data == "2":
        sleep(3)
        # system("clear")
        print(game_text_generator(story.story_dict["lock_door"]))
        return lock_door(option_choice())


def lock_door(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        print("\nSuccess!")
        sleep(3)
        system("clear")
        wardrobe_story = customise_story(story.story_dict["wardrobe"],
                                         story.user["name"])
        wardrobe_text = game_text_generator(wardrobe_story)
        print(wardrobe_text)
        return continue_chapter3()
    if data == "2":
        sleep(3)
        system("clear")
        print(game_text_generator(story.story_dict["fight_soldier"]))
        return end_game(main)


def continue_chapter3():
    """
    Takes the user to Chapter 3 or executes end_game()
    based on user input.
    """
    question = proceed_to_game(
               "Would you like to continue to Chapter 3 (y/n)? ")
    if question == "y":
        print("\nComing soon - stay tuned, Deary!")
        return end_game(main)
    elif question == "n":
        return end_game(main)


# def game_loop():
    """
    generates text and options over and over.
    """
# print("game loop works?")
# return path_selector()


# Reused variables
instructions = game_text_generator(story.story_dict["game_instructions"])

# Runs the game:
main()

# selection_generator(option, instruction_text, begin_story)
