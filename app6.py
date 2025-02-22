import streamlit as st

# Bakery Menu (Item Name and Price)
menu = {
    "Croissant": 2.5,
    "Chocolate Cake": 15.0,
    "Blueberry Muffin": 3.0,
    "cheesecase per piece": 5.0,
    "Banana Bread": 4.5,
}

st.title("🍰 Bakery Order Management")
st.write("Welcome to our bakery! Select your favorite items and place an order. 🎂🥐")

order = {}

for item, price in menu.items():
    col1, col2 = st.columns([2, 1])
    with col1:
        selected = st.checkbox(f"{item} - ${price}")
    with col2:
        if selected:
            quantity = st.number_input(f"Qty: {item}", min_value=1, max_value=10, step=1, key=item)
            order[item] = (price, quantity)

# Place Order Button
if st.button("🛒 Place Order"):
    if order:
        st.subheader("Order Summary")
        total = 0
        for item, (price, qty) in order.items():
            cost = price * qty
            total += cost
            st.write(f"{item} x {qty} = ${cost:.2f}")
        
        st.subheader(f"Total Bill: ${total:.2f}")
        st.success("Order placed successfully! Thank you for shopping with us.")
    else:
        st.warning("Please select at least one item to place an order.")



