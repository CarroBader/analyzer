
"""
This program will help you analyze txt files. 
"""
import menu

def main():
    """
    Starts the program.
    """
    file_name = "phil.txt"
    while True:
        choice = menu.menu_choice(file_name)
        if choice is False:
            break
        
        if choice != file_name:
            file_name = choice

if __name__ == "__main__":
    main()
