import streamlit as st
import os
import pandas as pd

# File to store expenses
FILE_NAME = "expenses.csv"

# Load expenses from file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return pd.DataFrame(columns=["Amount", "Category", "Description"])
    
    return pd.read_csv(FILE_NAME)

# Save expenses to file
def save_expenses(expenses_df):
    expenses_df.to_csv(FILE_NAME, index=False)

# Streamlit UI
st.title("💰 Expense Tracker App")

# Load existing expenses
expenses = load_expenses()

# Add a new expense
st.subheader("➕ Add a New Expense")
amount = st.number_input("Amount (in $):", min_value=0.01, format="%.2f")
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
description = st.text_input("Description (Optional)")

if st.button("Add Expense"):
    if amount:
        new_expense = pd.DataFrame([[amount, category, description]], columns=["Amount", "Category", "Description"])
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
        save_expenses(expenses)
        st.success("✅ Expense added!")
        st.rerun()

# Show expense list
st.subheader("📋 Your Expenses")
if not expenses.empty:
    st.dataframe(expenses)

    # Remove selected expenses
    st.subheader("🗑 Remove Expenses")
    indices = st.multiselect("Select expenses to remove", expenses.index.tolist())

    if st.button("Remove Selected"):
        expenses = expenses.drop(indices).reset_index(drop=True)
        save_expenses(expenses)
        st.success("✅ Selected expenses removed!")
        st.rerun()
else:
    st.info("No expenses added yet. Start tracking now!")

# Show total spending
st.subheader("📊 Total Spending: $ {:.2f}".format(expenses["Amount"].sum() if not expenses.empty else 0.00))

# Show spending by category
if not expenses.empty:
    st.subheader("📌 Spending by Category")
    category_summary = expenses.groupby("Category")["Amount"].sum()
    st.bar_chart(category_summary)

