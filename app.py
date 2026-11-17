import streamlit as st

st.title("SME Smart Operations")

st.subheader("Business Overview")

price = 8
quantity = 5

revenue = price * quantity

st.metric(
    "Today's Revenue",
    f"RM {revenue:.2f}"
)