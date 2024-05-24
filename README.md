# Once Upon a Time...
(By Laura Kondrataite)

Are you a fan of fairy tales, and even more so of Disney..?

Then, you are in luck! 

Join us and relive the events of the popular American TV show "Once Upon A Time". 

"Once Upon a Time..." is a text-based game that recreates the pilot episode of the show allowing the user to play out the sequence of events by choosing multiple options. 

The game incorporates the user's data to make it more interactive and make the user part of story-telling, as if they were the hero of the show!

The link to live gameplay can be found [here](https://once-upon-a-time-f214671524cd.herokuapp.com/).

## Table of Contents

[How to Play](#how-to-play)

[Design](#design)
- [Target Audience](#target-audience)
- [User Stories](#user-stories)
- [Flowcharts](#flowcharts)

[Features](#features)
- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

[Tools and Technologies](#tools-and-technologies)
- [Languages Used](#languages-used)
- [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)

[Testing](#testing)

[Deployment](#deployment)
- [Github](#github)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Heroku](#heroku)

[Credits](#credits)

## How to play



## Design
### Target Audience

The main target audience for the game is anyone aged 16 and over, who enjoys text-based adventures, and/ or is a fan of the TV Show and Disney fairytales.


### User Stories
**First Time User**

- As a first time user, I want to clearly see what the application is about.
- As a first time user, I want to be able to read instructions before progressing to the application.
- As a first time user, I want to be able to decide whether to proceed with the game after reading instructions.

<br>

- As a user, I want to be able to skip the instructions and go straight to the game.
- As a user, I want to see the game customised based on my name and gender.
- As a user, I want to be able to decide to finish the game once reached a certain stage of the game.
As a user, I want to be able to proceed to the next stage of the game after the first part is finished.
- As a user, I want to return to the main screen after the game has finished.

### Flowcharts
I used [Lucidchart](https://lucid.app/) for creating the logic and structure for the game. The game flow/logic of the project was split to two flowcharts (minimum viable product & future feature) due to limited use of blocks per one chart. Chapter 3 flowchart is a future feature. 

- MVP flowchart:

![flowchart-mvp](documentation/flowcharts/mvp-flowchart.jpeg)


- Future feature flowchart:

![flowchart-mvp](documentation/flowcharts/chapter3.jpeg)

## Features
### Existing Features
### Features Left to Implement

[Return to Table of Contents](#table-of-contents)
## Tools and Technologies

### Languages Used

- The primary language used for developing this project was Python.
- Markdown was used for creating the README and TESTING files.

### Frameworks, Libraries and Programs Used

The following resources were used to help implement the website:
- [Lucidchart](https://lucid.app/) for creating flowchart of the game
- [GitHub](https://github.com/) for creating and storing files and folders of the website
- **Git** was used for version control
- **VScode** editor for writing the code
- [CI Python Linter](https://pep8ci.herokuapp.com/#) for validating and checking my code for best code practices 
- [Heroku](https://www.heroku.com) for accessing and storing my application game
- I used the following libraries for the project:
    - **gspread** allowed to access, edit and manipulate data stored in the Google worksheets  
    - **google.oauth2.service_account** allowed to set up the authentication needed to access my GOOGLE cloud project
    - **time** module's sleep function allows to manipulate the timeframe when to display the game content 
    - **os** library system method allowed to clear the screen for better user experience when displayin the game


 [Return to Table of Contents](#table-of-contents)

## Testing
[testing.md](TESTING.md)

[Return to Table of Contents](#table-of-contents)

## Deployment
This website was deployed using GitHub pages an Heroku website. To deploy the project, follow the steps below:

### Github
1. Login to GitHub and navigate to the main repository page.
2.  Click on the chosen repository [Once-Upon-A-Time](https://github.com/laurakond/Once-Upon-a-Time).
3. Once inside the repository, click on the "Settings" tab above the repository title displayed around the middle of the page.
4. Select "Pages" tab on the left side navigation menu.
5. In the "Source" section (middle of the screen), select "main" or "master" branch, then "root" folder and click "save" button.
6. The GitHub page site will be deployed.

It might take a few minutes to generate the "live" website link.

The live link to the game can be found [Once-Upon-A-Time](https://once-upon-a-time-f214671524cd.herokuapp.com/).

#### How to Fork
To fork the repository in Github:
1. Follow steps 1 & 2 as above. 
2. Once inside the chosen repository, click the "fork" button in the top right corner above the "About section".

#### How to Clone
To clone the repository in Github:
1.  Follow steps 1 & 2 as in the deployment section above.
2.  Click on the "Code" button (often a bright color that stands out) in the top right corner just above the "commits" history. 
    - Select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
3.  Open the terminal in your chosen code editor and change the current working directory to the location you want to use for the cloned directory.
4.  Type 'git clone' into the terminal and then paste the copied link and press enter.

### Heroku
To deploy to the Heroku website, follow the steps below:
1. Navigate to https://www.heroku.com platform website.
2. Create or log in to your account.
3. Once on your dashboard:
    a. if you don't have any projects created yet, there should be a "Create a new app" prompt in the middle of the screen.
    b. if you have some projects already, click on the "New" tab on the top right corner of the screen just below the profile bauble. 
4.  Enter a unique application name for your project and select the region you are based in. Click "create app".
5. Once insde the app, select "Settings" button from the menu in the middle. It's important to edit the "Settings" tab before deploying the project: 
    1. Click on "Reveal Config Vars" and enter the following:
        
        a. if you are using any APIs you will need to copy paste your creds.json details:
        - in the "key" box type "CREDS" 
        - in the "value" box copy the contents of your creds.json file 
        - click "Add"

        b. type in PORT to the "key" box, and 8000 to the "value" box:
        - click "Add"

    2. Add Buildpacks below Config Vars. Click on "Add buildpack":

        a. First, select Python and click "Add buildpack".
 
        b. Second, select node.js and click "Add buildpack".
        
        **Note:** Python has to be positioned first (at the top) of the two packs.
6. Once step 5 is done, navigate to the "Deploy" tab a the top of the screen to the left of where the Settings tab is located.
7. Click on "Github" icon under "Deployment method", and connect Heroku to your Github account. 
8. Once the accounts are connected you can choose between automatic or manual deployment:

    a. Automatic deplyoment will automatically update your app once you use "git push" command in  your IDE. 

    b. Manual deployment will require you to manually "push" the changes you made in the IDE to the Heroku system.

[Return to Table of Contents](#table-of-contents)

## Credits

Refactoring:

- I used the following discussion board for refactoring user_input() function as moving the code to a second line was raising an error:
    - https://discuss.python.org/t/struggling-with-while-loops/20865/10
- The following article has given an idea how to refactor option_choice() function:
    - https://www.freecodecamp.org/news/best-practices-for-refactoring-code/

Data Validation resources:
https://www.w3schools.com/python/python_try_except.asp
https://www.w3schools.com/python/ref_string_isalpha.asp
https://www.w3schools.com/python/ref_string_isnumeric.asp
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3/library/stdtypes.html#str.isdigit
https://stackoverflow.com/questions/16399721/making-sure-no-integers-in-a-string
https://p-kane.medium.com/input-validation-with-python-570953d5d297


Acsii resources:

discussion thread that helped to make the design print: https://stackoverflow.com/questions/23623288/print-full-ascii-art

Information on how to print ascii art: https://www.youtube.com/watch?v=arcFqEuV_XQ

Once Upon a time TV show information and some of the content borrowed from there:
https://en.wikipedia.org/wiki/Pilot_(Once_Upon_a_Time)

Dictionary iteration:
https://www.geeksforgeeks.org/python-accessing-items-in-lists-within-dictionary/
https://realpython.com/iterate-through-dictionary-python/

[Return to Table of Contents](#table-of-contents)