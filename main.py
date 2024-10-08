from kresleni import spirala, random_shape,zprava,jednicka

def main_menu():

    operation = input('''
Select operation:
[1]- Spiral
[2]- Random
[3]- Message
[4]- Number one
[0]- Exit 

''')
    mylist = []

    if operation == '1':
        print("Program vykresli sprialu: ")
        spirala()
        

    elif operation == '2':
        print("Program vykresli neco nahodneho: ")       
        random_shape()

    elif operation == '3':
        print("Program vykresli zpravu pro uzivatele")
        zprava()

    elif operation == '4':
        print("Program vykresli jednicku")
        jednicka()
    elif operation == '0':
        print("Program se vypne.")

    else:
        print('You have not chosen a valid operator, please run the program again.')

    again()

def again():
    list_again = input('''
Would you like to see main menu again? (Y/N)
''')

    if list_again.upper() == 'Y':
        main_menu()
    elif list_again.upper() == 'N':
        print('OK. Bye bye. :)')
    else:
        again()

main_menu()
