# Write your code to expect a terminal of 80 characters wide and 24 rows high
import story

def user_input():
    """
    Asks user to input relevant data and stores it for in game use.
    """
    
    user_name = input("What is your name? ").capitalize()
    #user_gender = input("What is your gender? ")

    print(user_name)
    #print(user_gender)
    
    input_data_validation(user_name)
    #input_data_validation(user_gender)


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
                f"{data}")
        elif len(data)<3 or len(data)>15:
            raise ValueError(
                "Your entry must be between 3 to 15 characters long.")
    except ValueError as e:
        print(
            f"Invalid input: {e}. Please use letters only to fill in the fields.")
        print("Try again")
        





user_input()


























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