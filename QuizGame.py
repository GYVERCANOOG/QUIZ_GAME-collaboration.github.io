Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("""                       WELCOME TO OUR QUIZ GAME!
                       (PYTHON PROGRAMMING TRIVIA)""")
name = input("Enter your name: ")
print("\nWelcome", name, "! Thank you for participating our game !")
print("""NOTE:
    Each Items contains 5 points, be sure to put the correct answer. 
There are three different difficulties; Easy, Moderate, and Hard. In every level,
in order to proceed to the next level, you need to reach the passing score.
The level will repeat if you fail until you get the right answer and passed the level.
The passing total score is 40/50(80%). \n""")
start = input("-->(ENTER)\n")
while True:
    print("START!")
    print("\n----------------------Difficulty: EASY----------------------")

    total = 0
    ans1 = '=='
    q1 = input("\nQ1. What is th symbol for 'equal-to'?\n>>> ")
    if q1 >= ans1:
        print("Correct!\n")
        total += 5
    else:
        print("Sorry wrong guess.\nCorrect answer is '=='\n")

    ans2 = '%'
    q2 = input("Q2. What is the symbol for modulos?\n>>> ")
    if q2 == ans2:
        print("Correct\n")
        total += 5
    else:
        print("Sorry, wrong guess")
        print("Correct Answer is '%'\n")

    ans3 = '*'
    q3 = input("Q3. What is the symbol for multiplication?\n>>> ")
    if q3 == ans3:
        print("Correct!\n")
        total += 5
    else:
        print("Sorry, wrong guess"
              "Answer is '*'\n")

    print("Total score in EASY Level is:", total, "/ 15")
    print("Passing score is 10\n")

    eas_totals = 10
    while True:
        for games in range(1):
            if total == 15:
                print("***PERFECT!!!***")
            if eas_totals <= total:
                print("You Passed!\n"
                      "Let's proceed to MODERATE Level.\n-->(ENTER)")

                start_2 = input("")

                while True:
                    print("------------------------------Difficulty: MODERATE------------------------------")

                    total_2 = 0
                    ans_1 = 'A'
                    q_1 = input("""
Q1. What is the code for this output
['Cow', 'Dog', 'Cat']
['Cow', 'Dog', 'Cat']
['Cow', 'Dog', 'Cat']

[A].                                     [B]. 
name_list=["Cow","Dog", "Cat"]           name_list=["Cow","Dog", "Cat"]
for x in name_list:                      For x in names_list:
    print(name_list)                     print(name_list)
>>> """)
                    if q_1 >= ans_1 and q_1 == 'a':
                        print("Correct!\n")
                        total_2 += 5
                    else:
                        print("Sorry, wrong guess")
                        print("Correct Answer is A.\n")

                    ans_2 = 'B'
                    q_2 = input("""Q2.
1  count=0
2  for i in range(1, 5):
3  	if i%2 != 0:
4          count+=1
5         print(i)
6  print("We have ",count,"odd")
7
8
-->What will be the output?

[A].Error       [B]. 1               [C]. 1  
                     3                    2
                     We have 2 odd        3 
                                          4
                                          We have 2 odd 
\n>>> """)
                    if q_2 == ans_2 or q_2 == 'b':
                        print("Correct!\n")
                        total_2 += 5
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is B.\n")

                    ans_3 = 'A'
                    q_3 = input("""Q3.What will be the output of the code?

1  OnlineGames = ['Mobile legend', 'Call of duty ', 'Dota 2', 'Apex legend']
2  for i in range(len(OnlineGames)):
3      print("I love playing this game ", OnlineGames[i])

[A]. I love playing this game Mobile legend
   I love playing this game Call of duty
   I love playing this game Dota 2
   I love playing this game Apex legend

[B]. I love playing this game Mobile legend Call of duty Dota 2 Apex legend
>>> """)
                    if q_3 == ans_3 or q_3 == 'a':
                        print("Correct!\n")
                        total_2 += 5
                    else:
                        print("Sorry, wrong guess."
                              "Correct answer is A.\n")

                    print("Total score in MODERATE level is ", total_2, "/ 15")
                    print("Passing score is 10.\n")

                    med_totals = 10
                    while True:
                        for game_2 in range(1):
                            if total_2 == 15:
                                print("***PERFECT!!!***")
                            if med_totals <= total_2:
                                print("You Passed!\n"
                                      "Let's proceed to HARD Level.\n-->(ENTER)")
                                start_3 = input("")
                                while True:
                                    print("------------------------------Difficulty: HARD------------------------------")

                                    total_3 = 0
                                    print("""\nQ1. _____ / __________ _________ is used when a program needs to repeatedly process 
one or more instructions until some condition
is met, at which time the loops end.""")
                                    q_4 = input("\n>>> ").lower()
                                    if q_4 == 'loop' or q_4 == 'loops' or q_4 == 'repetition structure':
                                        print("Correct!\n")
                                        total_3 += 5
                                    else:
                                        print("Sorry, wrong guess."
                                              "Correct answer is 'Loop' or 'Repetition Structure'.\n")

                                    print("Q2. Python has three primitive loop command. List one.")
                                    q_5 = input("\n>>> ").lower()
                                    if q_5 == 'nested loops' or q_5 == 'while loops' or q_5 == 'for loops':
                                        print("Correct!\n")
                                        total_3 += 5
                                    else:
                                        print("Sorry, wrong guess."
                                              "Correct answer is For loops, While Loops, and Nested loops\n")

                                    ans_6 = "A"
                                    print("""Q3. What is 'Input'?          
a. Data entered into a program, either by the programmer or digitally.
b. Strings entered into a program, either by the programmer or digitally.
c. Data entered into a program, either by the bugs.
d. Loops entered into a program, either by the bugs.\n""")
                                    q_6 = input(">>> ".lower())
                                    if q_6 == ans_6 or q_6 == 'a':
                                        print("Correct!\n")
                                        total_3 += 5
                                    else:
                                        print("Sorry, wrong guess."
                                              "Correct answer is A.\n")

                                    ans__2 = "february"
                                    dat = "20"
                                    yer = "1991"
                                    print("NOTE: Month and Date has 2 points and Year has 1 point.")
                                    q__2 = input("Q4. When was the Python programming language created?\nJanuary	July\nFebruary   August\nMarch	  September\nApril	  October\nMay	    November\nJune	   December\nEnter Month >>> ").lower()
                                    Q2_2 = input("Enter date >>> ")
                                    Q2_3 = input("Enter the year>>> ")
                                    if q__2 == ans__2:
                                        total_3 += 2
                                    if Q2_2 == dat:
                                        total_3 += 2
                                    if Q2_3 == yer:
                                        total_3 += 1
                                        print("Correct!")
                                    else:
                                        print("Sorry, wrong guess.")
                                        print("Correct Answer is February 20 1991")
                                    print("""\nPython was created and first released on February 20, 1991.
While you may know the python as a large snake,
the name of the Python programming language comes from an old 
BBC television comedy sketch series called Monty Python's Flying Circus.\n""")

                                    print("Total score in HARD Level is:", total_3,"/ 20")
                                    print("Passing score is 15")

                                    har_totals = 15
                                    passed = True
                                    while True:
                                        for okay in range(1):
                                            if total_3 == 20:
                                                print("***PERFECT!!!***")
                                            if har_totals <= total_3:
                                                print("You Passed!\n\n")
                                                print("You COMPLETED the Game,", name, "!")
                                                print("Congratulations!!!")
                                                print("Total Scores:", total + total_2 + total_3, "/ 50")
                                                average = total + total_2 + total_3
                                                if average == 50:
                                                    print("Remarks:EXCELLENT!\nWell Done.")
                                                elif average >= 40:
                                                    print("Remarks:PASSED\nNot Bad.")
                                                elif average >= 32:
                                                    print("""You didn't reach the passing score 
which is 40. leoBetter luck next time""",name,"""
Maybe this game is not for you.
Thank you for Playing:)""")
                                                else:
                                                    print("FAILED")
                                                exit()
                                        else:
                                            print("Failed\nTry Again")
                                        break
                        else:
                            print("Failed\n"
                                  "Try Again")
                            break
        else:
            print("Failed\n"
                  "Try Again")
            break
