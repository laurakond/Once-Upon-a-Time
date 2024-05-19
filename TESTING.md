# Testing for Once Upon a Time 
By Laura Kondrataite

## Contents

[Testing](#testing)

- [PEP8 Linter](#pep8-linter)
- [Bugs](#bugs)
	- [Fixed bugs](#fixed-bugs)
	- [Unfixed bugs](#unfixed-bugs)
- [Lighthouse](#lighthouse)
- [User stories testing](#user-stories-testing)
- [Accessibility](#accessibility)
- [Browser testing](#browser-testing)
- [Responsiveness testing](#responsiveness-testing)
- [User testing](#user-testing)
- [Manual testing](#manual-testing)

## Testing
- When working on user input data validation, I had to include an additional if clause for the gender data in order to validate specific words that the user required to enter. 

    In order to make it work, I had to change "or" to "and" statement, otherwise the code was continuously looping regardless if the correct input was provided.

- function def game_text_generator(data), was trowing a result "None" when the following code was used:

        for line in data:
    	print(line)

    I resolved this by adding a new variable text and asigning each line iteration to it. However, the terminal then started returning each line without starting them on a new line. I resolved this by adding "\n" at the end of each line in the story.py file.

- when testing the code after implementing run_chapter1() function, the code printed "None" output. This was because I used print() statement inside the function. 
    - I resolved this by changing print() with return statement. (see image - chapter1-None-error)
    - this error came back again and to solve it temporarily I put return chapter1 below print(chapter1)

- I had difficulty to make the code generate appropriate text content and functionality. I realised that there was an error in proceed_go_game() function as it collated two separate steps in one. Therefore, I decided to separate into two functions, one responsible just for generating the user input and validating it using validation function. The other function, continue_to_play(data), I used to generate appropriate content based on user selection in the previous function.
    - This part of the code proved challenging as I was still getting unintentional functionality. After trying multiple ways of displaying text, I finally managed to get the code working as intended by printing game text and returning another function to trigger user input in order to progress along the way. 

            def  proceed_to_game():
            """
            This function runs after instructions and asks if the
            user wants to continue to play the game
            """
            while  True:
                question =  input("Would you like to play the game (y/n)? ").lower()
                if yes_no_validation(question):
            break
            return question
            
            
            def  continue_to_play(data):
            """
            generates appropriate game play functions based
            on user choice after reading instructions
            """
            if data =="y":
                user_input()
                print(game_text_generator(story.story_dict["story_intro"]))
                print(game_text_generator(story.story_dict["chapter1"]))
            return path_selector()
            
            elif data =="n":
            return end_game()
            

            def  path_selector():
            """
            generates a question for the user to select relative path
            to progress the game accordingly.
            """
            while  True:
                first_question =  input("Type '1' or '2' to make a choice: ")
                if option_choice_validation(first_question)
                break
            return test(first_question)

        - At this stage the game functionality seems to have worked. 

- At the end of the game, the questions "Would you like to continue to Chapter 3 (y/n)?" was displaying twice if option "n" was selected. 
    - I resolved this by putting user_input_chpt3 into a variable and using it in the if statement inside continue_chapter3() function.

- When trying to implement game restart once the end_game() function was triggered, it was throwing an error "NameError: name 'main' is not defined. Did you mean: 'min'?". This was because the main() function was defined at the bottom of the code, i.e. after it was called in the game.
    - I resolved this by moving the main() to the top of the code, and calling it inside the end_game() function.

## PEP8 Linter

## Bugs
### Fixed bugs
### Unfixed bugs

## User stories testing

### Accessibility
### Browser testing
### Responsiveness testing
### User testing
### Manual testing