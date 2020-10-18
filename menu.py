"""
This file contains the menu for the analyze program.
"""

import analyzer

def menu_choice():
    """
    Containts the if-statment to reach the different functions.
    """
    file_name = "phil.txt"

    print("------------------------") 
    print("1 - Counts lines")
    print("2 - Counts words")
    print("3 - Counts letters")
    print("4 - Count word frequency")
    print("5 - Count letter frequency")
    print("6 - Does all above")
    print("7 - Change file")
    print("q - quit")
    print("------------------------") 

    choice = input("--> ") 


    # Choice 1 --- Counts lines
    if choice == "1":
        analyzer.count_lines(file_name)

    # Choice 2 --- Counts words
    elif choice == "2":
        words = analyzer.count_words(file_name)
        print("Words: " + str(words))

    # Choice 3 --- Counts letter
    elif choice == "3":
       letters = analyzer.count_letters(file_name)
       print("Letters: " + str(letters))

    # Choice 4 --- Count word frequency
    elif choice == "4":
        analyzer.word_frequency(file_name)

    # Choice 5 --- Count letter frequency
    elif choice == "5":
        analyzer.letter_frequency(file_name)

    # Choice 6 --- Does alla functions
    elif choice == "6":
        analyzer.all(file_name)

    # Choice 7--- Change file 
    elif choice == "7":
        new_name = analyzer.change_file()
        file_name = new_name
        print(file_name)

    elif choice == "q":
        return False 

    else:
        print("That is an invalid choice")

    input("\nPress enter to get more knowledge...")
