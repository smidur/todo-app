import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal11")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Ubuntu', 12))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=functions.get_todos())
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=functions.get_todos())
        except IndexError:
            sg.popup("Please, select an item first.", font=('Helvetica', 12))
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=functions.get_todos())
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please, select an item first.", font=('Helvetica', 12))
    elif event == "Exit":
        break

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
