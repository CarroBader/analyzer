
"""
This program will help you analyze txt files. 
"""
import menu

def main():
    """
    Starts the program.
    """
    while True:
        choice = menu.menu_choice()
        if choice == False:
            break

if __name__ == "__main__":
    main()