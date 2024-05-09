# Write your code to expect a terminal of 80 characters wide and 24 rows high
import story

def user_input():
    """
    Asks user to input relevant data and stores it for in game use.
    """
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