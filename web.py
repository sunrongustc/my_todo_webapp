import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = sl.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


sl.title("My todo APP")
sl.subheader("it is easy to use")
sl.write("And it is for everyone in the world!")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        index = todos.index(todo)
        todos.pop(index)
        del sl.session_state[todo]
        functions.write_todos(todos)
        sl.experimental_rerun()

sl.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")

