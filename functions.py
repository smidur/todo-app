FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a LIST of its contents
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes a LIST into a text file.
    Returns NONE
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Test")
    print(get_todos())