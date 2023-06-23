import functions
from datetime import datetime as dt

now = dt.now().strftime("%Y-%m-%d__%H-%M")
print("It is:", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action.strip()

    if user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}: {item.title()}"
            print(row)

    elif user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            change = input(f"Type a new todo instead of '{todos[number]}': ")
            todos[number] = change + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There's no item with that number.")
            continue

    elif user_action == "exit":
        break
    else:
        print("Invalid command.")




