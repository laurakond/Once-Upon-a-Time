# Write your code to expect a terminal of 80 characters wide and 24 rows high
import story
from time import sleep


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
    #user = {}

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
    
    story.user["name"] = user_name#user["name"] = user_name
    story.user["gender"] = user_name
    #user["gender"] = user_gender
    print(story.user)
    return story.user


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
    #else:
    elif data == "2":
        user_input()
        print(game_text_generator(story.story_dict["story_intro"]))
        print(game_text_generator(story.story_dict["chapter1"]))
        #return game_loop()
        return chapter1(path_selector())
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
        #return game_loop()
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


def path_selector():
    """
    generates a question for the user to select relative path
    to progress the game accordingly.
    """
    while True:
        in_game_question = input("Type '1' or '2' to make a choice: ")
        if option_choice_validation(in_game_question):
            break

    return in_game_question


def chapter1(data):
    """
    generates appropriate game play based on option selection.
    """
    if data == "1":
        print("curse comes, game over")
        #print(test)
        return end_game()
    elif data == "2":
        print(game_text_generator(story.story_dict["rumpel"]))
        #print(game_text_generator(story.story_dict["chapter1_cont"]))
        #custom_name = [line.replace("{user_name}", user["name"]) for line in story.story_intro]
        #return game_text_generator(custom_name)
        return rumpel(path_selector())


def rumpel(data):
    """
    returns appropriate result after chapter1 continued.
    """
    if data == "1":
        print(game_text_generator(story.story_dict["baby_name"]))
        return baby_name(path_selector())
    if data == "2":
        print("chapter1_cont test option2")
        print("curse comes, game over")
        #print(test)
        return end_game()


def baby_name(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        print("chapter1_cont test option1")
        print("curse comes, game over")
        #print(test)
        return end_game()
    if data == "2":
        print("chapter2 test option2")
        print(game_text_generator(story.story_dict["secret_door"]))
        return secret_door(path_selector())


def secret_door(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        print("chapter2_cont test option1")
        print("curse comes, game over")
        #print(test)
        return end_game()
    if data == "2":
        print("chapter2_cont test option2")
        print(game_text_generator(story.story_dict["lock_door"]))
        return lock_door(path_selector())


def lock_door(data):
    """
    returns appropriate result after chapter2.
    """
    if data == "1":
        print("you won!")
        print(game_text_generator(story.story_dict["wardrobe"]))
        return chapter3()
    if data == "2":
        print("chapter2_cont2 test option1")
        print("curse comes, game over")
        #print(test)
        return end_game()


def user_input_chpt3():
    """
    returns question if the user wants to carry on with the story.
    """
    question = input("Would you like to continue to Chapter 3 (y/n)? ")
    if yes_no_validation(question):
            #print("yes no validation works")
            break
        
    return question


def contninue_chapter3(data):
    """
    Executes appropriate actions based on user input for 
    chapter 3.
    """
    if move_to_chapter3 =="y":
        print("Coming soon - stay tuned, Deary!")
        return end_game()
    elif move_to_chapter3 =="n":
        return end_game()


def game_loop():
    """
    generates text and options over and over
    """
    print("game loop works?")
    return path_selector()
    #path_selector()


welcome_screen()
option = option_choice()
move_to_chapter3 = user_input_chpt3()
instruction_or_game(option)
#sleep(3)
#selection_generator(option, instruction_text, begin_story)
