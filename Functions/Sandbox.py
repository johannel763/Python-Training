## takes name and surname

## calls first_last function

def main():
    print('Hello! Please enter your first and last name..')
    first_name = str(input('First name: '))
    last_name = str(input('Last name: '))
    greeting(first_name, last_name)


def greeting(first, last):
    print('Welcome', first, last,  '!')

main()