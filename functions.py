FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    # read file
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# todos_arg is non-default argument and filepath_arg is a default argument
def write_todos(todos_arg, filepath=FILEPATH):
    # create a file or write on existing file
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
