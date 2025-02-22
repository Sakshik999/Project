import streamlit as st
import os

# Load existing tasks
def load_tasks():
    if not os.path.exists("tasks.txt"):
        return []
    
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
    
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

# Streamlit UI
st.title("📝 To-Do List App")

tasks = load_tasks()

# Add a new task
new_task = st.text_input("Add a task:")
if st.button("Add Task"):
    if new_task.strip():  # Avoid empty tasks
        if new_task not in tasks:  # Prevent duplicates
            tasks.append(new_task)
            save_tasks(tasks)
            st.success(f"✅ Task '{new_task}' added!")
            st.rerun()  # Updated fix
        else:
            st.warning("⚠️ Task already exists!")

# Show tasks with checkboxes
st.subheader("Your Tasks:")
completed_tasks = []

if tasks:
    for index, task in enumerate(tasks):
        if st.checkbox(task, key=f"task_{index}"):
            completed_tasks.append(task)
else:
    st.write("🎉 No tasks pending!")

# Remove completed tasks
if st.button("Remove Completed"):
    if completed_tasks:
        tasks = [task for task in tasks if task not in completed_tasks]
        save_tasks(tasks)
        st.success("✅ Completed tasks removed!")
        st.rerun()  # Updated fix
    else:
        st.warning("⚠️ No tasks selected for removal!")
