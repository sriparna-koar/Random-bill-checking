import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.messagebox as tsmg

# Menu data
menus = {
    "Indian": {
        "Dosa": 5.99,
        "Idly": 4.99,
        "Samosa": 3.99,
        "Paratha": 6.99,
    },
    "American": {
        "Burger": 6.99,
        "Hot Dog": 4.99,
        "Pizza": 7.99,
        "Fries": 2.99,
    },
    "Japanese": {
        "Sushi": 8.99,
        "Tempura": 7.99,
        "Ramen": 9.99,
        "Teriyaki": 8.99,
    },
    "Other Cuisine": {
        "Spaghetti": 7.99,
        "Taco": 5.99,
        "Shawarma": 8.99,
        "Kebab": 7.99,
    },
}
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # Allow only .txt files
    if file_path:
        with open(file_path, 'r') as file:
            input_text = file.read()
            details_text.delete("1.0", "end")
            details_text.insert("1.0", input_text)



def order():
    selected_item = ""
    for item, item_var in items.items():
        if item_var.get():
            selected_item = item
            break

    if not selected_item:
        tsmg.showwarning("Order Warning", "Please select an item.")
        return

    customer_name = name_entry.get()
    customer_contact = contact_entry.get()
    restaurant_name = restaurant_name_entry.get()
    restaurant_address = address_entry.get()
    cuisine_type = selected_cuisine.get()
    additional_details = details_text.get("1.0", "end-1c")

    if cuisine_type == "Select Cuisine":
        tsmg.showwarning("Order Warning", "Please select a cuisine type.")
        return

    selected_menu = menus[cuisine_type]

    order_message = f"Customer Name: {customer_name}\n"
    order_message += f"Contact Details: {customer_contact}\n"
    order_message += f"Restaurant Name: {restaurant_name}\n"
    order_message += f"Restaurant Address: {restaurant_address}\n"
    order_message += f"Cuisine Type: {cuisine_type}\n\n"
    order_message += "Selected Menu:\n"

    total_price = 0

    for item, item_var in items.items():
        if item_var.get():
            item_price = selected_menu.get(item, 0)
            order_message += f"{item}: ${item_price:.2f}\n"
            total_price += item_price

    order_message += "Additional Details:\n"
    order_message += additional_details

    order_message += f"\nTotal Price: ${total_price:.2f}"

    tsmg.showinfo("Order Received", order_message)


# Create the main application window
root = tk.Tk()
root.geometry("455x700")
root.title("Restaurant Order App")

# Set the style for widgets
style = ttk.Style()
style.configure("TLabel", font=("lucida", 14, "bold"))
style.configure("TEntry", font=("lucida", 12))
style.configure("TButton", font=("lucida", 12))
style.configure("TCheckbutton", font=("lucida", 12))
style.configure("TMenubutton", font=("lucida", 12))

# Customer information
name_label = ttk.Label(root, text="Customer Name:")
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()

contact_label = ttk.Label(root, text="Contact Details:")
contact_label.pack()
contact_entry = ttk.Entry(root)
contact_entry.pack()

restaurant_name_label = ttk.Label(root, text="Restaurant Name:")
restaurant_name_label.pack()
restaurant_name_entry = ttk.Entry(root)
restaurant_name_entry.pack()

address_label = ttk.Label(root, text="Restaurant Address:")
address_label.pack()
address_entry = ttk.Entry(root)
address_entry.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

# Menu items
label_frame = ttk.LabelFrame(root, text="What would you like to order?")
label_frame.pack()

items = {
    "Dosa": tk.IntVar(),
    "Idly": tk.IntVar(),
    "Samosa": tk.IntVar(),
    "Paratha": tk.IntVar(),
}

for item, item_var in items.items():
    ttk.Checkbutton(label_frame, text=item, variable=item_var).pack(anchor="w")

# Cuisine selection
cuisine_label = ttk.Label(root, text="Select Cuisine Type:")
cuisine_label.pack()

cuisine_options = ["Select Cuisine", "Indian", "American", "Japanese", "Other Cuisine"]
selected_cuisine = tk.StringVar()
selected_cuisine.set("Select Cuisine")
cuisine_dropdown = ttk.OptionMenu(root, selected_cuisine, *cuisine_options)
cuisine_dropdown.pack()

# Additional details and buttons
details_label = ttk.Label(root, text="Additional Details:")
details_label.pack()
details_text = tk.Text(root, height=5, width=40)
details_text.pack()

order_button = ttk.Button(root, text="Place Order", command=order)
browse_file_button = ttk.Button(root, text="Browse File", command=browse_file)
order_button.pack()

root.mainloop()
