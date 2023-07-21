import streamlit as st

# Define your menu items as a list of tuples (menu_item_name, ingredient_1, ingredient_2, ...)
menu_items = [
    ("Pizza", "Dough", "Tomato Sauce", "Cheese", "Toppings"),
    ("Burger", "Bun", "Patty", "Lettuce", "Cheese", "Tomato", "Onion"),
    ("Pasta", "Pasta", "Tomato Sauce", "Meatballs", "Cheese"),
]

def calculate_ingredients(menu_item, num_people):
    st.write(f"Menu Item: {menu_item}")
    st.write(f"Number of People: {num_people}")

    # Assuming each menu item requires one unit of each ingredient per person
    for ingredient in menu_item[1:]:
        ingredient_quantity = num_people
        st.write(f"{ingredient}: {ingredient_quantity} units")

def main():
    st.title("Menu Ingredients Calculator")

    # Dropdown for selecting the menu item
    selected_menu_item = st.selectbox("Select Menu Item", menu_items)

    # Number input for the number of people
    num_people = st.number_input("Enter the Number of People", min_value=1, value=1)

    # Calculate and display the ingredients
    if st.button("Calculate"):
        calculate_ingredients(selected_menu_item, num_people)

if __name__ == "__main__":
    main()