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

def option_choice():
    """
    Runs every time the user needs to select a choice
    from given options during game play.
    """
    choice = input("Type '1' or '2' here to proceed: ")


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
                print("works?")
            else:
                input_data_validation(user_gender)
                break
    
    user["name"] = user_name
    user["gender"] = user_gender

    return user
        

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




game_start()
option_choice()

test = user_input()
print(test)


























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