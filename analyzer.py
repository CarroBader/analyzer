"""
This file contains all functions for the menu choices.
"""

def count_lines(file):
    """
    Counts the none empty lines in a file.
    """
    try:
        file_open = open(file)  
    except:
        print("There is no such file:", file_open)
        exit() 

    count = 0
    for line in file_open:
        if line != '\n':
            count += 1
    
    print("Lines: " + str(count))

    file_open.close()


def count_words(file):
    """
    Counts the words in the file.
    """

    try:
        file_open = open(file)  
    except:
        print("There is no such file:", file_open)
        exit() 

    file_read = file_open.read()

    file_trimmed = file_read.replace(',','').replace('.','').replace('-','')

    file_array = file_trimmed.split(' ')

    count = 0
    for word in file_array:
        count += 1
    
    return count

    file_open.close()


def count_letters(file):
    """
    Counts the letters in the file.
    """
    try:
        file_open = open(file)  
    except:
        print("There is no such file:", file_open)
        exit() 

    file_read = file_open.read()

    file_trimmed = file_read.replace(' ','').replace('\n','').replace(',','').replace('.','').replace('-','')

    return len(file_trimmed)

    file_open.close()

def word_frequency(file):
    """
    Prints word frequency in the file.
    """
    
    word_dict = {}

    try:
        file_open = open(file)  
    except:
        print("There is no such file:", file_open)
        exit() 
    
    words = count_words(file)

    file_read = file_open.read()

    file_trimmed = file_read.replace(',','').replace('.','').replace('-','').replace('\n', '')

    file_list = file_trimmed.split(' ')

    for i, word in enumerate(file_list):
        word_lower = word.lower()
        if word_lower not in word_dict:
            word_dict[word_lower] = 1
        else:
            word_dict[word_lower] += 1


    for key, value in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:7]:
        procentage = round(value / words * 100, 1)
        
        print(key + ": " + str(value) + " | " + str(procentage) + "%")

    file_open.close()

def letter_frequency(file):
    """
    Prints letter frequency in the file.
    """
    
    letter_dict = {}

    try:
        file_open = open(file)  
    except:
        print("There is no such file:", file_open)
        exit() 
    
    letters = count_letters(file)

    file_read = file_open.read()

    file_trimmed = file_read.replace(',','').replace('.','').replace('-','').replace('\n', '').replace(' ', '')

    file_list = list(file_trimmed)

    for i, letter in enumerate(file_list):
        letter_lower = letter.lower()
        if letter_lower not in letter_dict:
            letter_dict[letter_lower] = 1
        else:
            letter_dict[letter_lower] += 1

    for key, value in sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)[:7]:
        procentage = round(value / letters * 100, 1)
        
        print(key + ": " + str(value) + " | " + str(procentage) + "%")

    file_open.close()

def all(file):
    count_lines(file)
    print(" ")
    words = count_words(file)
    print("Words: " + str(words))
    print(" ")
    letters = count_letters(file)
    print("Letters: " + str(letters))
    print(" ")
    word_frequency(file)
    print(" ")
    letter_frequency(file)


def change_file():
    """
    Changes the text-file used for the program.
    """
    user_input = input("What is the name of the new file?  Ex.file.txt\n")
    print("The new file is now " + user_input)
    return user_input