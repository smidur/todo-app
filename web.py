import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todo = todo.strip()
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""

st.title('To-Do App')
st.subheader('This is To-Do App')
st.write("This app is to increase your productivity")

# for todo, key in zip(todos, range(len(todos))):
#     st.checkbox(todo, key=key)
for todo in todos:
    st.checkbox(todo)

st.text_input(label="label", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')

