import database

menu_prompt = """

    Please Choose one of these opitons:

    1) Add a new bean.
    2) See all beans.
    3) Find a bean by name.
    4) See which preperation is best for a bean
    5)Exit.

    Your Selection
"""


def menu():
    connection = database.connect()
    database.create_table(connection)

    inp = 1

    while(inp):
        inp = input(menu_prompt)
        if inp == '1':
            name = input("Enter bean name: ")
            method = input("How you prepared the bean: ")
            rating = int(input("Enter your rating Score: "))
            database.add_bean(connection, name, method, rating)

        elif inp == '2':
            beans = database.get_all_beans_func(connection)
            for i in beans:
                print(f" {i[1]} ({i[2]}) - {i[3]}/100  ")

        elif inp == '3':
            name = input("Enter the bean name to find it: ")
            beans = database.get_beans_by_name_func(connection, name)
            for i in beans:
                print(f" {i[1]} ({i[2]}) - {i[3]}/100  ")

        elif inp == '4':
            name = input("Enter bean name: ")
            best_method = database.get_best_preperation_for_bean_func(
                connection, name)
            print(
                f"The best preperation method for {name} is {best_method[2]} ")

        elif inp == '5':
            exit(1)

        else:
            print("Enter a valied Input")


menu()
