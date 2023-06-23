FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a LIST of its contents
    """
    todos_local = []
    with open(filepath, "r") as file:
        todos_raw = file.readlines()
    for row in todos_raw:
        row = row.strip('\n')
        todos_local.append(row)
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes a LIST into a text file.
    Returns NONE
    """
    for row in todos_arg:
        todos_arg[todos_arg.index(row)] = row.title() + '\n'
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Test")
    print(get_todos())