# Andrea Safadi

# This program is directly inspired by, and is based in the fictional universe of the "SCP foundation".
# The SCP foundation is a website with a compilation of user-made creative tales of horror, mystery, and sometimes
# memes. These stories largely take place in a universe where supernatural or unexplained phenomena plague the earth.
# The 'SCP foundation' is supposedly a foundation that documents and contains these phenomena to
# protect the general public.
# In the early 2010's the website hosted an SCP generator, where the user was able to input words as they so wished
# within a template to create an SCP themselves. It could be as goofy or as serious as the user wished it to be.
# This generator however, at least to my knowledge, no longer exists.
# Part of this program will contain an 'SCP generator' somewhat similar to that one.
# The other part of the program is somewhat original, and
# is meant to indulge the user in a narrative experience.

# citations:
# 1 -- scp-wiki.wikidot.com
# 2 -- the-scp.foundation
# 3 -- w3schools.com
# 4 -- includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx
# 5 -- stackoverflow.com/questions/51151739/how-to-make-a-game-with-lives-in-python
# 6 -- m.youtube.com/watch?v=lm37J2Gyebg
# 7 -- m.youtube.com/watch?v=u0402sx05yl

#Lines 47 - 86 of code:
# the try, except, and continue statements were taken from an example posted on the includehelp.com website
# listed above (4), but with minor changes and obviously pertaining to a completely different context.
# These were also inspired by a youtube video titled: "Input Validation in Python"(7).

# In lines 50, 62, and 70:
# The code structure for login was slightly inspired by a youtube video called
# "Python Practice: Number Guessing Game with While Loops & If Statements"(6).
# Meanwhile, the attempt function was inspired by the stack overflow website (5) listed above in citations.

# Explaining Operators:
# Numeric Operators: (Will come in the generator part of the program, but for now I will explain them here)
# -- (**) - Exponentiation: It will raise the integer to a power
             # - example) print(4**5) == 1024
# -- (*) - Multiplication: Will multiply two integers together and output the result
             # - example) print(4*5) == 20
# -- (/) - Division: Will divide two integers together and display the result as a floating point
            # - example) print(20/5) == 4.0
# -- (%) - Modulus: Will divide two integers together and display the remainder
            # - example) print(4%5) == 4
# -- (//) - Floor Division: Divides two integers together and rounds the result down to the nearest whole number
            # - example) print(20//5) == 4
# -- (+) - Addition: Adds two integers together and displays the result
            # - example) print(4+5) == 9
# -- (-) - Subtraction: Subtracts two integers together and displays the result
            # - example) print(4-5) == -1

# String Operators: *(Have been used in lines 86 and 118)*

# -- (+) - Concatenation: Essentially meshes two strings together to form one string, unless commas or spaces are
# used. Cannot be used with two different data types.
            # - example) print("Hello"+"World") == HelloWorld
# -- (*) - Repetition: Will concatenate a string a number of instances depending on the int it is multiplied by.
            # - example) print("Hello!" * 3) == Hello!Hello!Hello!

# *(sep and end arguments are visible in lines 104 - 107, and are used thereafter)*

# Lines 86 - 127 of code are the login part of the program, where the user is supposed to enter their
# government ID number and PIN. Being a high intelligence agency, however, the protocol is that
# you only have 3 attempts before you start looking a little suspicious. Of course, if you just happened to
# forget your login (I do all the time) then either you or an agent will override the system so you can
# attempt to login once more. Attempting to override incorrectly will tell the computer that there is
# something wrong and it will inevitably shut down the program. Can't have randos reading about
# ghosts.
# I've never programmed before, so in my humble opinion this is probably the coolest thing ever but that's
# just me.

# Andrea Safadi

# This program is directly inspired by, and is based in the fictional
# universe of the "SCP foundation". The SCP foundation is a website with a
# compilation of user-made creative tales of horror, mystery, and sometimes
# memes. These stories largely take place in a universe where supernatural
# or unexplained phenomena plague the earth. The 'SCP foundation' is
# supposedly a foundation that documents and contains these phenomena to
# protect the public. In the early 2010's the website hosted an SCP
# generator, where the user was able to input words as they so wished within
# a template to create an SCP themselves. It could be as goofy or as serious
# as the user wished it to be. This generator however, at least to my
# knowledge, no longer exists. Part of this program will contain an 'SCP
# generator' somewhat similar to that one. The other part of the program is
# somewhat original, and is meant to indulge the user in a narrative
# experience.

# citations: 1 -- scp-wiki.wikidot.com
# 2 -- the-scp.foundation
# 3 -- w3schools.com
# 4 -- includehelp.com/python/asking-the-user-for-integer
# -input-in-python-limit-the-user-to-input-only-integer-value.aspx
# 5 -- stackoverflow.com/questions/51151739/how-to-make-a-game-with-lives-in
# -python
# 6 -- m.youtube.com/watch?v=lm37J2Gyebg
# 7 -- m.youtube.com/watch?v=u0402sx05yl
# 8 -- https://discuss.codeacademy.com/t/print-statement-with-a-timer/607802
# 9 -- https://stackoverflow.com/questions/58775663/python-not-reading-file-
# correctly
# 10 -- https://www.freecodecamp.org/news/python-write-to-file-open-read-
# append-and-other-file-handling-functions-explained/amp/
# 11 -- https://stackoverflow.com/questions/19747371/python-exit-commands-why
# -so-many-and-when-should-each-be-used

# Lines 47 - 86 of code: the try, except, and continue statements were taken
# from an example posted on the includehelp.com website listed above (4),
# but with minor changes and obviously pertaining to a completely different
# context. These were also inspired by a YouTube video titled: "Input
# Validation in Python"(7).

# In lines 50, 62, and 70: The code structure for login was slightly
# inspired by a YouTube video called "Python Practice: Number Guessing Game
# with While Loops & If Statements"(6). Meanwhile, the attempt function was
# inspired by the stack overflow website (5) listed above in citations.

# lines 220 to 228, 268 to 277, 396 to 398, and 421 to 452: The import time
# module and the use of the sleep function from the time library was taken
# from the website in citation (8).

# Line 395: the use of the seek() function for files was taken from the website
# in citation (9).

# Line 290: The use of "w+", or just adding a + in general for editing and
# reading files was taken from the website in citation (10).

# Lines 217 and 221: raise SystemExit was taken from the website in citation
# (11).

# Explaining Operators: Numeric Operators: (Will come in the generator part
# of the program, but for now I will explain them here)
# -- (**) - Exponentiation: It will raise the integer to a power
# - example) print(4**5) == 1024
# -- (*) - Multiplication: Will multiply two integers together
# and output the result
# - example) print(4*5) == 20
# -- (/) - Division: Will divide two integers together and display the
# result as a floating point
# - example) print(20/5) == 4.0
# -- (%) - Modulus: Will divide two integers together and display the remainder
# - example) print(4%5) == 4
# -- (//) - Floor Division: Divides two integers together and rounds the
# result down to the nearest whole number
# - example) print(20//5) == 4
# -- (+) - Addition: Adds two integers together and displays the result
# - example) print(4+5) == 9
# -- (-) - Subtraction: Subtracts two integers together and displays the result
# - example) print(4-5) == -1

# String Operators: *(Have been used in lines 86 and 118)*

# -- (+) - Concatenation: Essentially meshes two strings together to form
# one string, unless commas or spaces are used. Cannot be used with two
# different data types.
# - example) print("Hello"+"World") == HelloWorld
# -- (*) - Repetition: Will concatenate a string a number of instances
# depending on the int it is multiplied by.
# - example) print("Hello!" * 3) == Hello!Hello!Hello!

# *(sep and end arguments are visible in lines 104 - 107, and are used
# thereafter)*

# Lines 86 - 127 of code are the login part of the program, where the user
# is supposed to enter their government ID number and PIN. Being a high
# intelligence agency, however, the protocol is that you only have 3
# attempts before you start looking a little suspicious. Of course, if you
# just happened to forget your login (I do all the time) then either you or
# an agent will override the system, so you can attempt to log in once more.
# Attempting to override incorrectly will tell the computer that there is
# something wrong, and it will inevitably shut down the program. Can't have
# randos reading about ghosts. I've never programmed before, so in my humble
# opinion this is probably the coolest thing ever but that's just me.

# programs for grading purposes:

#uncomment to test! use of boolean (not), !=, and the for in range() function.

# print("[Countdown]")
# for x in range(10, -1, -1):
#     if x != 0:
#         print(x)
#     else:
#         print("blastoff!")
#
# print("\n[Even or Odd?]")
# x = int(input("\ninput a number: "))
# y = int(input("input a second number: "))
#
# subtract = y - x
# if subtract % 2 != 0:
#     subtract = not True
# else:
#     subtract = True
# print(x, "minus", y, "equals an even number; True or False?", subtract)


def failed_attempt():
    print("\nREMAIN SEATED WITH YOUR HANDS IN FULL VIEW. "
          "AN AGENT WILL COME TO RETRIEVE YOU FOR QUESTIONING. "
          "\nYOU HAVE USED UP THE LEGAL NUMBER"
          " OF ATTEMPTS.")
    try:
        int(input("\noverride: "))
        print("\nWARNING. THIS IS YOUR LAST LOGIN ATTEMPT. "
              "FAILURE TO PROVIDE VALID CREDENTIALS WILL RESULT"
              " IN EMERGENCY SHUTDOWN. "
              "\nIf you are a staff member and require "
              "assistance, please refer to your supervisor for"
              " login.")
        Gov_ID = input("\nGovernment ID number: ")
        Pass_word = input("\nPIN: ")
        ID = int(Gov_ID)
        PIN = int(Pass_word)
        if len(Gov_ID) == 9 and len(Pass_word) == 6:
            menu_success()
        else:
            print("ERROR, input was not valid. Please remain seated."
                  "\n" * 100)
            raise SystemExit
    except ValueError:
        print("ERROR, input was not valid. Please remain seated."
              "\n" * 100)
        raise SystemExit


def menu_success():
    import time
    User_Name = "Dr. Ethan Briar"
    print("\n" + "\n....." + "\n"), time.sleep(1), print("\nCREDENTIALS "
                                                         "ACCEPTED",
                                                         end="_"), time.sleep(
        2)
    print("\n" + "\n-", "Welcome to the SCP Foundation", "-",
          sep="-------", end=""), time.sleep(2)
    print("\n" + "\nYou are now logged in as", User_Name, "\n"
                                                          "Clearance Level: 3"),
    time.sleep(3),
    print("\n", "Menu", "", sep="_"), time.sleep(1), print("\n[Guide]",
                                                           "\n[SCP Directory]",
                                                           "\n[K-Class "
                                                           "Scenarios]",
                                                           "\n[Files]",
                                                           "\n[D̸A̷T̤́A̢E̶̥X̦̀PUNGE̩D"
                                                           "̟́]̶̀ ̶̧͔̀͋̍",
                                                           "\n[O-5 Directory]"),
    time.sleep(1)
    print(
        "\nFor our new staff members: It is highly recommended to "
        "read our foundation's Guide before commencing operations.")


def login_attempt():
    continue_looping = True
    login = 3
    while continue_looping:
        try:
            Gov_ID = input("\nGovernment ID number: ")
            Pass_word = input("\nPIN: ")
            ID = int(Gov_ID)
            PIN = int(Pass_word)
            if len(Gov_ID) == 9 and len(Pass_word) == 6:
                menu_success()
                continue_looping = False
            else:
                login = login - 1
                if login > 0:
                    print("\nINVALID CHARACTER LENGTH. PLEASE TRY AGAIN.\n"
                          "\nID should be 9 digits in length."
                          "\nPIN should be 6 digits in length.\n"
                          "\nyou have", login, "attempts left.")
            if login < 1:
                continue_looping = False
                failed_attempt()
        except ValueError:
            login = login - 1
            if login < 1:
                continue_looping = False
                failed_attempt()
            else:
                print("\nINVALID CREDENTIALS. PLEASE TRY AGAIN.", "\nyou have",
                      login, "attempts left.")


def plain_menu():
    import time
    print("\n", "Menu", "", sep="_"), time.sleep(1), print("\n[Guide]",
                                                           "\n[SCP Directory]",
                                                           "\n[K-Class "
                                                           "Scenarios]",
                                                           "\n[Files]",
                                                           "\n[D̸A̷T̤́A̢E̶̥X"
                                                           "̦̀PUNGE̩D "
                                                           "̟́]̶̀ ̶̧͔̀͋̍",
                                                           "\n[O-5 Directory]"),
    time.sleep(1),
    print(
        "\nFor our new staff members: It is highly recommended to "
        "read our foundation's Guide before commencing operations.")


def main_menu():
    import time
    menu_options = ["Guide", "SCP Directory", "K-Class Scenarios", "Files",
                    "surprise me :)!", "0-5 Directory", "Menu"]
    loop_menu = True
    while loop_menu:
        command = input("\nPlease enter a command from the menu: ")
        Menu_Choice = open(str(command), "w+")
        if (command == menu_options[0]) or (command == "guide"):
            Menu_Choice.write(
                "------------------------------------------------------------"
                "------------------------------------\n"
                "\nSCP's are otherworldly phenomena that inhabit "
                "the earth and are regulated by the "
                "SCP foundation. \nThis organization heavily "
                "reinforces the importance of the acronym which "
                "represents our name and our purpose. "
                "\nSecure. Contain. Protect."
                "\nWhen referring to the containment of unnatural "
                "phenomena, \nSCP's are arranged into different "
                "classes depending on their inherent effects and "
                "danger to society."
                "\n"
                "\nThese classes include:"
                "\n"
                "\n-- SAFE: anomalies that are easily and safely "
                "contained. \nThis can be due to either extensive "
                "research and understanding of the SCP, or due to the "
                "anomaly only activating in response to "
                "specific triggers. "
                "\nThis does NOT, however, mean the SCP "
                "itself is considered 'safe'."
                "\n"
                "\n-- EUCLID: anomalies that require more resources to "
                "contain completely. \nThis is due to the unpredictable "
                "nature of the SCP, and minimal understanding. "
                "\nThese SCP's tend to be "
                "sentient/autonomous."
                "\n"
                "\n-- KETER: anomalies that are exceedingly difficult to "
                "contain reliably, with containment "
                "procedures often being extensive. "
                "\nThis can be due to a "
                "lack of technology or understanding required for "
                "containment."
                "\nThese SCP's are not necessarily dangerous, "
                "just difficult."
                "\n"
                "\n-- THAUMIEL: anomalies that are used to contain other SCP's"
                " that couldn't be contained otherwise. "
                "\nThese are classified at the highest levels of the "
                "SCP foundation."
                "\n"
                "\n-- NEUTRALIZED: anomalies that are no longer anomalous, "
                "due to having been intentionally \nor accidentally "
                "destroyed/disabled."
                "\n"
                "\n-- APOLLYON: anomalies that cannot be contained or are "
                "expected to breach containment. \nThese are usually "
                "associated with apocalyptic events, or a K-Class "
                "scenario of some kind, and require a massive amount of "
                "effort to deal with. "
                "\n"
                "\n{*Note: The term 'K-class scenario' refers to different "
                "types of apocalyptic events. \nPlease refer to the "
                "[K-Class Scenarios] page on our site's menu for "
                " \nfurther information on the different subtypes and their "
                "descriptions.}"
                "\n"
                "\n-- ARCHON: anomalies that could theoretically be contained,"
                " but are best left uncontained for reasons. "
                "\nThey may be part of consensus reality that is either "
                "difficult or may have adverse effects if "
                "contained. \nThese are specifically chosen not to be "
                "contained."
                "\n"
                "\n"
                "------------------------------------------------------------"
                "------------------------------------"
                "\n[FOR HELP WITH CLASSIFYING AN SCP, PLEASE REFER TO THE"
                " 'LOCK AND BOX' TEST BELOW]: \n"
                "-------------------------------------------------------------"
                "-----------------------------------"
                "\n"
                "\n* If you lock it in a box, leave it alone, and nothing "
                "bad will happen, \nthen it is classified as SAFE."
                "\n"
                "\n* If you lock it in a box, leave it alone, and you're "
                "not entirely sure what will happen, \nthen it is "
                "classified as EUCLID."
                "\n"
                "\n* If you lock it in a box, leave it alone, and it "
                "easily escapes, \nthen it is classified as KETER. "
                "\n"
                "\n* If it is the box, then it is classified as THAUMIEL."
                "\n"
                "\n* If you can't fit it in a box, and it contains the"
                " capacity to induce an apocalyptic event, \nthen it is"
                " classified as APOLLYON."
                "\n"
                "\n* If you could have locked it in a box but chose not to,"
                " \nthen it is classified as ARCHON."
                "\n"
                "\nRemember again that these classes have nothing to do "
                "with danger, ONLY containment."
                "\nThe SCP Foundation will hold no responsibility for "
                "\ncasualties caused by failure to follow these "
                "procedures."
                "\n"
                "\n"
                "------------------------------------------------------------- "
                "-----------------------------------")
            Menu_Choice.seek(0)
            print("\n."), time.sleep(1), print("\n."), time.sleep(1),
            print("\n."), time.sleep(2)
            print(Menu_Choice.read())
        elif (command == menu_options[1]) or (command == "scp"):
            Menu_Choice = open(str(command), "w+")
            Menu_Choice.write("-----------------------------"
                              "------------------------------- "
                              "------------------------------------\n"
                              "\n{THE SCP DIRECTORY}\n"
                              "DOCUMENT ARCHIVES:"
                              "")
        elif command == menu_options[2]:
            pass
        elif command == menu_options[3]:
            pass
        elif command == menu_options[4]:
            pass
        elif command == menu_options[5]:
            pass
        elif command == menu_options[6] or command == "menu":
            plain_menu()
        else:
            print("Invalid input. Command was not derived from the menu.")


import time

print("\nWARNING"), time.sleep(1),
print("\nTHE PAGE YOU ARE ABOUT TO ACCESS CONTAINS CLASSIFIED GOVERNMENT "
      "INFORMATION"), time.sleep(4),
print("\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣴⣤⣤⣤⣤⣤⡄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⠟⢋⣵⣿⣿⣿⡿⠛⣩⣤⣿⣿⣿⣿⣿⣿⣿⣬⣙⠻⣿⣿⣿⣷⡍⠛⢿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⠟⢹⠃⣠⣾⣿⣿⡿⢋⣴⣿⣿⣿⣿⠿⠿⠈⠿⢿⣿⣿⣿⣷⣤⡙⣿⣿⣿⢦⡀⢣⠙⣿⣿⣿⣿"
      "\n⣿⣿⡿⡿⠀⡯⠊⣡⣿⣿⠏⣴⣿⣿⣿⠟⠁⣀⣤⣤⠀⣤⣤⡀⠙⠻⣿⣿⣿⣌⢻⣿⣧⡉⠺⡄⢸⠹⣿⣿"
      "\n⣿⣿⠃⢷⠀⡠⢺⣿⣿⡏⣰⣿⣿⡟⠁⣠⣾⣿⣿⠿⠀⠿⣿⣿⣷⡄⠘⣿⣿⣿⡄⣿⣿⣯⠢⡀⢸⠀⢹⣿"
      "\n⣿⣿⠀⢸⠊⣠⣿⣿⣿⢀⣿⣿⣿⠁⣰⣿⣿⣿⣿⣆⢀⣼⣿⣿⣿⣿⡄⢸⣿⣿⣿⣹⣿⣿⣦⠈⢺⠀⢸⣿"
      "\n⣿⠹⡆⠀⣴⢻⣿⣿⣿⢸⣿⣿⣿⠀⣿⣿⡿⠿⠿⢿⣿⠿⠿⠿⣿⣿⡇⢈⣿⣿⣿⠀⣿⣿⣿⠳⡀⢀⡇⢸"
      "\n⣿⡀⠹⣸⠉⣿⣿⡿⢋⣠⣿⣿⣿⡀⠸⠟⢋⣀⢠⣾⣿⣷⡀⣀⡙⠻⠁⢸⣿⣿⣿⣈⠻⣿⣿⡄⠹⡜⠀⣸"
      "\n⣿⢧⠀⠇⢠⣿⣿⣷⡘⣿⣿⣿⣟⣁⡀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠿⠀⣠⣉⣿⣿⣿⡿⢠⣿⡿⢧⠀⠁⣰⢿"
      "\n⣿⡌⢷⡄⣾⠀⣿⣿⣷⡜⢿⣿⣿⣿⣿⣦⣄⠈⠉⠛⠛⠛⠉⢁⣠⣾⣿⣿⣿⣿⡟⣰⣿⣿⡇⢸⢀⡴⠃⣼"
      "\n⣿⣷⣄⠙⢿⠀⣿⢿⣿⣿⣌⠿⠟⡻⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⡿⠛⠿⠟⣼⣿⡿⢫⠃⢸⠋⢀⣼⣿"
      "\n⣿⣿⣟⣶⣄⡀⢸⡀⢻⣿⣿⣾⣿⣿⣶⣍⣙⠛⠿⠿⠿⠿⠿⠛⣋⣥⣶⣿⣿⣾⣿⣿⠁⣸⢀⣴⣶⣯⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⠾⣧⠀⢯⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⠃⢠⢷⣛⣉⣽⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣄⣁⡈⢧⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⢋⣀⣠⣴⣾⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣯⣉⠉⠉⠉⣀⣀⡭⠟⠛⢛⣛⠛⠛⠛⣛⠛⠛⠩⣥⣀⣈⢁⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⡛⢉⣁⣀⣤⠖⣫⣴⣿⣿⣷⣬⡙⣦⣤⣀⡈⣉⣩⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
      "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"), time.sleep(1),
print("\nANY ACCESS BY UNAUTHORIZED PERSONNEL IS STRICTLY PROHIBITED"),
time.sleep(3),
print(
    "\nFAILURE TO COMPLY WILL RESULT IN CRIMINAL PENALTIES, "
    "INCLUDING BUT NOT LIMITED TO LIFE-LONG DETAINMENT AND/OR EXECUTION"),
time.sleep(5),
print("\nYOU HAVE BEEN WARNED\n"), time.sleep(5),

login_attempt()
main_menu()

# For use later on:
#
# - Bolded text:
# print("\033[1m"+"hullo"+"\033[0m")
# print()
# print("\nhullo")

# import random
# scp_list = ["Awaiting De-classification [Blocked]", "The 'Living' Room",
#                 "Biological Motherboard", "The 12 Rusty Keys and the Door",
#                 "Fountain of Youth", "Zombie Plague", "Red Ice",
#                 "Shadow Person", "Game Show of Death", "The Gate Guardian",
#             "The Stairwell", "There Was A Crooked Man", "An Empty World",
#             "The Body Farm", "RONALD REAGAN [DATA EXPUNGED] WHILE TALKING",
#             "The Yule Man", "Antique Chess Computer", "Cabinet Maze",
#             "Special Personnel Requirements [\nRESTRICTED FOR AGENTS BELOW"
#             " CLEARANCE LEVEL 5]", "MalO ver1.0.0", "A Cowbell", ]
# for scp in range(0,10):
