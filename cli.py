# todo list project
# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b-%d-%Y: %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # calling get todos function to read the todos
        todos = functions.get_todos()

        # add the file into the list
        todos.append(todo + "\n")

        # # calling rewrite function to write the todos
        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith("show"):
        # calling get todos function to read the todos
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            # removing extra spaces
            item = item.strip('\n')
            index = index + 1
            print(f'{index}-{item.capitalize()}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            # calling get todos function to read the todos
            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            # calling rewrite function to write the todos
            functions.write_todos(todos, 'todos.txt')

            print('Todo is updated successfully')

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            # calling get todos function to read the todos
            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            # calling rewrite function to write the todos
            functions.write_todos(todos, 'todos.txt')

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("There is no item with that number. ")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Please choose the above commands only!!")
print("Bye!!")
