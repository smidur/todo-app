import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do",
                   layout=[[label, input_box, add_button]],
                   font=('Ubuntu', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event.startswith("Add"):
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    elif sg.WINDOW_CLOSED:
        break

window.close()
