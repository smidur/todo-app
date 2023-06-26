import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("To-Do",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Ubuntu', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=functions.get_todos())

    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=functions.get_todos())

    elif event == "todos":
        window['todo'].update(value=values['todos'][0])

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
