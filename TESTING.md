# Testing for Once Upon a Time 
By Laura Kondrataite

# Table of Contents

## Testing
- When working on user input data validation, I had to include an additional if clause for the gender data in order to validate specific words that the user required to enter. 

    In order to make it work, I had to change "or" to "and" statement, otherwise the code was continuously looping regardless if the correct input was provided.

- function def game_text_generator(data), was trowing a result "None" when the following code was used:

        for line in data:
    	print(line)

    I resolved this by adding a new variable text and asigning each line iteration to it. However, the terminal then started returning each line without starting them on a new line. I resolved this by adding "\n" at the end of each line in the story.py file.

- when testing the code after implementing run_chapter1() function, the code printed "None" output. This was because I used print() statement inside the function. 
    - I resolved this by changing print() with return statement. (see image - chapter1-None-error)