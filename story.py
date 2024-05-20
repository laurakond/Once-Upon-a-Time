user = {
 "name": "",
 "gender": "",
}


story_dict = {
    "game_intro": ["\nWelcome to an interactive story-based game. It was ",
                   "inspired by a popular TV Show 'Once Upon a Time'. \n",
                   "Please choose from the following two options. \n",
                   "1. Read instructions",
                   "2. Go to the story\n\n"],
    "game_instructions": ["\nWhen you start the game, you will need to enter \n",
                          "your name and gender. This will customise the \n",
                          "game play. Once inside the story, you will be \n",
                          "prompted to choose between two options to see \n",
                          "the outcome of the game. Enter your preferred \n",
                          "option and see if you win!\n\n"
                          "Enjoy, and good luck!\n\n"],
    "story_intro": ["...in a far away land, there lived Snow White with her \n",
                    "prince charming. After defeating the Evil Queen, peace \n",
                    "was brought to their Kingdom. Snow White and Prince \n",
                    "Charming were happily expecting an addition to their\n",
                    "family - a little baby called {user_name}.\n\n",
                    "Alas, their joy was shortlived. The Evil Queen \n",
                    "announced she was brewing a curse. The curse that \n",
                    "would trap the kingdom in her fantasy world in \n",
                    "a far away land. A city called StoryBrooke, in Maine, \n",
                    "USA… where all fairytale characters would be trapped \n",
                    "in unhappy stories, clueless of who they really are. \n",
                    "Worried about the hapless future, Snow and Charming \n",
                    "set out to stop the Evil Queen.\n"],
    "chapter1": [#"Chapter 1\n\n",
                 "They searched for solutions and ways to stop her.\n",
                 "Rumours reached that Rumpelstiltskin would be able\n",
                 "to help them. Yet, Snow was aware of his 'dealings', \n",
                 "and was cautious to approach him. \n\n",
                 "Should Snow and Charming:\n\n",
                 "1. Confront the Queen.\n",
                 "2. Speak to Rumpelstinskin.\n"],
    "confront_queen": ["    ###########################     \n",
                       "\nSnow decides to speak to the Evil Queen again, \n",
                       "hoping to change her mind. Unfortunately, her plea \n",
                       "is not heard and the Queen proceeds with her plan. \n",
                       "The curse comes and everyone in the Kingdom is \n",
                       "banished for life.\n\nYou were unsuccessful!\n",
                       "\n    ###########################     \n"],
    "rumpel": ["\nSnow decides to speak to Rumpel. Upon the visit,\n",
               "he explains that the only way to save them all,\n",
               "was for Snow White to hide in a magical wardrobe \n",
               "so she could be transported to the unknown land. \n",
               "However, there was one condition attached. \n",
               "\nRumpel asked for the baby’s name:\n\n",
               "1. Snow decides to tell the baby’s name.\n",
               "2. Snow does not disclose the name.\n"],
    "no_name": ["\nSnow did not want to owe Rupel anything. Disclosing the \n",
                "name of the baby would have put them in harms' way \n",
                "regardless. Unfortunately, they had no other solution.\n\n",
                "The curse comes and everyone in the Kingdom is banished \n",
                "for life.\n\nYou were unsuccessful!"],
    "chapter2": [#"\nChapter 2\n\n",
                  "On the day of the planned escape, a purple curse cloud \n",
                  "arose… The Queen’s Army has stormed the Castle, \n",
                  "forcing Snow and Charming to rush to the wardrobe. \n",
                  "Alas, their baby decided to come.\n\n",
                  "The army is at the end of the corridor. \n\n",
                  "Should Snow and Charming:\n\n",
                  "1. Fight the Queen's army.\n",
                  "2. Escape through the secret door.\n"],
    "fight_army": ["\nCharming marches towards the army to protect Snow \n",
                   "and their child. Yet, the army is too vast, and all \n",
                   "three of them are captured. The curse comes and \n",
                   "everyone in the Kingdom is banished for life.\n",
                   "\nYou were unsuccessful!"],
    "secret_door": ["\nThey run down the secret stairs one level below \n",
                    "where the wardrobe room is located. Snow and Charming \n",
                    "are noticed by a soldier who starts marching their ",
                    "way:\n\n"
                    "1. Charming fights the soldier.\n",
                    "2. Charming locks the door.\n"],
    "fight_soldier": ["\nCharming marches towards the soldier to protect \n",
                      "Snow and their child. Yet, the soldier is too \n",
                      "strong. Charming falls injured, while Snow and ",
                      "the baby are captured.\n\n"
                      "The curse comes and everyone in the Kingdom is \n",
                      "banished for life.\n",
                      "\nYou were unsuccessful!"],
    "lock_door": ["\nThe locked door gives them a few precious moments.\n",
                  "While the soldier is trying to break in, Snow and \n",
                  "the baby step into the wardrobe. But it does not work..!\n",
                  "The soldier manages to break through the door: \n\n",
                  "1. Snow places the baby in the wardrobe.\n",
                  "2. Charming fights the soldier.\n"],
    "wardrobe": ["\nJust as the wardrobe door shuts, the soldier breaks \n",
                 "through. Charming marches to protect Snow, alas, he \n",
                 "falls injured. Both Snow and Charming are captured and \n"
                 "are taken to the Queen. \n\nThe curse is released and ",
                 "the fairytale characters find themselves\nin StoryBrooke, ",
                 "where they are stripped of their memories and living \n",
                 "hapless lives, while the Queen revels in her \n",
                 "accomplishment.\n\nBut hope is not yet lost, ",
                 "as {user_name} has managed to escape. \nWill the curse ",
                 "be broken?\n"]
}

ascii_dict = {
    "title_logo": [r"""         
  ___                _   _
 / _ \ _ _  __ ___  | | | |_ __  ___ _ _
| (_) | ' \/ _/ -_) | |_| | '_ \/ _ \ ' \
 \___/|_||_\__\___|  \___/| .__/\___/_||_|
  __ _  | |_(_)_ __  ___   |_|
 / _` | |  _| | '  \/ -_)_ _ _
 \__,_|  \__|_|_|_|_\___(_|_|_)
 
 """],
    "instructions": [r"""
 _  _              _              _           
| || |_____ __ __ | |_ ___   _ __| |__ _ _  _ 
| __ / _ \ V  V / |  _/ _ \ | '_ \ / _` | || |
|_||_\___/\_/\_/   \__\___/ | .__/_\__,_|\_, |
                             |_|          |__/ 
    """],
    "chapter1": [r"""
  ___ _              _             _ 
 / __| |_  __ _ _ __| |_ ___ _ _  / |
| (__| ' \/ _` | '_ \  _/ -_) '_| | |
 \___|_||_\__,_| .__/\__\___|_|   |_|
               |_|                   

    """],
    "chapter2": [r"""
    
  ___ _              _             ___ 
 / __| |_  __ _ _ __| |_ ___ _ _  |_  )
| (__| ' \/ _` | '_ \  _/ -_) '_|  / / 
 \___|_||_\__,_| .__/\__\___|_|   /___|
               |_|                     

    """]
}
