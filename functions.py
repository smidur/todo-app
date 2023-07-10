FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a LIST of its contents
    """
    todos_local = []
    with open(filepath, "r") as file:
        todos_raw = file.readlines()
        todos_local = [todo.strip("\n") for todo in todos_raw]
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes a LIST into a text file.
    Returns NONE
    """
    todos_arg = [item.title() + "\n" for item in todos_arg]
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Test")
    print(get_todos())