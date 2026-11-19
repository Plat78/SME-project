
import streamlit as st

# Dashboard title
st.title("SME Smart Operations")
st.subheader("Product Registration")

# Initialise product storage
if "products" not in st.session_state:
    st.session_state.products = []

# Initialise Product ID counter
if "next_id" not in st.session_state:
    st.session_state.next_id = 1

# User input section
product_name = st.text_input("Product Name")

product_price = st.number_input(
    "Selling Price (RM)",
    min_value=0.0,
    value=0.0,
    step=0.5
)

product_stock = st.number_input(
    "Available Stock",
    min_value=0,
    value=0,
    step=1
)

reorder_level = st.number_input(
    "Reorder Level",
    min_value=0,
    value=5,
    step=1
)

# Registration button
if st.button("Register Product"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")

    elif product_price <= 0:
        st.warning("Selling price must be greater than zero.")

    else:
        product_id = f"P{st.session_state.next_id:03d}"

        new_product = {
            "Product ID": product_id,
            "Product": product_name.strip(),
            "Price (RM)": product_price,
            "Stock": product_stock,
            "Reorder Level": reorder_level
        }

        st.session_state.products.append(new_product)

        st.session_state.next_id += 1

        st.success("Product registered successfully!")

# Display registered products
st.subheader("Registered Products")

if st.session_state.products:
    st.dataframe(
        st.session_state.products,
        use_container_width=True
    )
else:
    st.info("No products registered yet.")
