import Create, Delete, Display, Modify, Search

def menu():
        print('MENU:')
        print('  1 - Create')
        print('  2 - Modify')
        print('  3 - Search')
        print('  4 - Display')
        print('  5 - Delete')
        print('  M - Display menu again')
        print('  E - EXIT')

menu()

while True:
        choice = input('\nChoose an option: ')
        print()
        if choice == '1':
                Create.create()
        elif choice == '2':
                Modify.modify()
        elif choice == '3':
                Search.search()
        elif choice == '4':
                Display.display()
        elif choice == '5':
                Delete.delete()
        elif choice.upper() == 'M':
                menu()
        elif choice.upper() == 'E':
                break
        else:
                print('Wrong choice. Enter again')
