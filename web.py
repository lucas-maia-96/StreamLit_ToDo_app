import streamlit as st 
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"]
    if todo_local not in todos and todo_local:
        todos.append(todo_local + '\n')
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your produtivity.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    
st.text_input(label="New:", placeholder="Add new todo..", 
              on_change=add_todo, key='new_todo') 
